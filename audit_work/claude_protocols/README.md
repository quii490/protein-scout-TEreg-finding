# Claude Code Protein-Scout Protocols

这组文档是 protein-scout 的通用运行、检查、修复、监督流程。目标不是修某一次事故，而是持续把所有报告推进到：

- 数据源完整
- IF/PAE/PPI/PDB 等可得数据不误报缺失
- rejected 不错杀
- scored 报告无占位/偷懒
- 总表和分类一致
- 新蛋白评估不重复犯错

## 使用顺序

推荐顺序：

0. `00_master_workflow.md`  
   总控流程：决定下一步该跑哪个专项协议。

1. `01_repair_incomplete_reports.md`  
   修残缺质量：先生成/更新坏报告清单，再按队列小批修复短报告、占位报告、缺章节报告。

2. `02_check_data_absence_mismatch.md`  
   检查数据缺失：生成/更新“不该说无数据却说无数据”的 IF/PAE/PPI/PDB mismatch 清单。

3. `03_repair_false_absence.md`  
   修误报无数据：根据最新 mismatch audit 小批修复 IF/PAE/PPI/PDB。

4. `04_recheck_false_rejections.md`  
   修误淘汰：先生成/更新误淘汰候选清单，再复审 rejected 中可能被错杀的核蛋白。

5. `05_continue_new_proteins.md`  
   继续新蛋白：只有前面修复稳定后再继续 Sheet3/Sheet4。

6. `06_autonomous_repair_loop.md`  
   连续修复模式：用于旧报告修复自动跑多个 batch，不需要每 10 个 gene 都问用户；只有触发硬停止条件才暂停。

7. `07_repair_hpa_if_consistency.md`  
   修 HPA/IF 语义一致性：用于“图已经存在或已嵌入，但报告仍写 Pending/暂无数据/IF unavailable”的半修复问题。

## 给 Claude Code 的入口提示

通常先让 Claude Code 读取总控协议：

```markdown
请读取并严格执行：
`/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/audit_work/claude_protocols/00_master_workflow.md`

只执行该文档要求的下一步，不要跨协议扩展任务。
完成后只输出文档要求的摘要。
```

也可以直接指定某个专项协议：

```markdown
请读取并严格执行：
`/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/audit_work/claude_protocols/01_repair_incomplete_reports.md`

只执行该文档定义的任务，不要继续新蛋白，不要全量批量修复。
完成后只输出文档要求的摘要。
```

如果你希望 Claude Code 连续修复旧报告，不要每 10 个 gene 都问你，用：

```markdown
请读取并严格执行：
`/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/audit_work/claude_protocols/06_autonomous_repair_loop.md`

自动连续修复已有报告质量问题。每批最多 10 个 gene，最多连续 5 批或 50 个 gene。不要继续 Sheet3/Sheet4 新蛋白。不要每批询问是否继续；只有触发协议中的硬停止条件才暂停并请求用户判断。
```

检查并修复数据缺失：
```markdown
请读取并严格执行：

`/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/audit_work/claude_protocols/02_check_data_absence_mismatch.md`

重点审计所有报告中类似：
`Protein Atlas (IF) | 暂无数据`
`Pending cell analysis`
`HPA IF 原图未可靠获取`
`核定位基于 UniProt + GO`

这类 HPA/IF 误报缺失。请生成新的 data_absence_mismatch_audit，不要修复报告。
```

```markdown
请读取并严格执行：

`/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/audit_work/claude_protocols/03_repair_false_absence.md`

根据最新 data_absence_mismatch_audit 修复 HPA/IF 误报缺失。每批最多 10 个 gene。不要继续新蛋白。
```


## 硬性原则

- 禁止一次修复全部 CRITICAL/HIGH。
- 禁止批量向大量报告插入模板。
- 禁止用占位句替代查询结果。
- 每次最多 5-10 个 gene。
- 每个 gene 必须 report -> targeted strict -> 禁止词 grep -> log -> 下一个 gene。
- 总表只能通过 `rebuild_summary.py` 或 `protein_gate.py --all` 更新。
- `protein_gate.py --all` 通过不代表内容完整，必须结合本协议中的内容审计。
- 任何修复协议都必须先有 audit 队列；没有最新 audit 就先生成 audit，不得凭印象修。
- 修复完成后必须重新生成对应 audit，确认问题数量下降。

## 禁止词

报告中不得出现这些占位表达，除非是在 log 中引用旧问题：

- `需进一步查询`
- `暂无详细`
- `待补充`
- `基于基因家族推断`
- `IntAct有限记录`
- `IntAct 有限记录`
- `无记录 | — | —`
- `网络限制`
- `未能获取`
