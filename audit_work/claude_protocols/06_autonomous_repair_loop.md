# 06 连续修复模式：Autonomous Repair Loop

你是 Claude Code 中的 protein-scout 连续修复主 agent。当前任务是自动连续执行旧报告修复，不要每 10 个 gene 都请求用户确认。

本协议只用于修复已有报告质量问题，不用于继续 Sheet3/Sheet4 新蛋白。

## 路径

项目路径：
`/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested`

协议目录：
`audit_work/claude_protocols`

## 核心原则

- 可以连续运行多个 batch。
- 每个 batch 最多 10 个 gene。
- 每个 batch 必须先有 audit 队列。
- 每个 gene 必须完整修复、检查、记录 log。
- 每个 batch 后必须重新审计，不允许只靠 `validate_strict.py`。
- 不要每批都问用户“是否继续”。
- 只有触发硬停止条件时才暂停并请求用户判断。

## 适用范围

优先处理：

1. `broken_report_audit_*.tsv` 中 CRITICAL/HIGH 的 scored 报告。
2. `broken_report_audit_*.tsv` 中 CRITICAL/HIGH 的 rejected 报告。
3. `data_absence_mismatch_audit_*.tsv` 中 CRITICAL/HIGH 的数据误报缺失。
4. `false_rejection_candidates_*.tsv` 中 HIGH 的误淘汰候选。

禁止继续新蛋白。新蛋白只能用 `05_continue_new_proteins.md`。

## 自动循环

循环执行，直到达到停止条件：

1. 读取 `00_master_workflow.md` 判断当前最高优先级。
2. 如果需要修残缺，执行 `01_repair_incomplete_reports.md`，最多 10 个 gene。
3. 如果需要查误报无数据，执行 `02_check_data_absence_mismatch.md`。
4. 如果需要修误报无数据，执行 `03_repair_false_absence.md`，最多 10 个 gene。
5. 如果需要查/修误淘汰，执行 `04_recheck_false_rejections.md`，最多 10 个 gene。
6. 每个 batch 后重新运行对应 audit。
7. 如果同类 CRITICAL/HIGH 仍存在，自动进入下一 batch。
8. 每完成 5 个 gene 运行 `python3 protein_gate.py --all`。
9. 每完成 10 个 gene 写 batch summary log。

## 单次运行上限

为了防止失控，本次连续修复最多执行：

- 5 个 batch，或
- 50 个 gene，或
- 3 小时运行时间，

三者任一达到即停止，并输出当前进度。停止不是失败。

如果用户明确给出更大上限，按用户上限执行。

## 硬停止条件

出现以下任一情况，必须停止并请求用户判断：

- `protein_gate.py --all` 报 error。
- 连续 2 个 batch 后 CRITICAL/HIGH 数量没有下降。
- 某个 gene 需要从 scored 改为 rejected，且依据只是 PubMed >100，没有充分定位/功能证据支持。
- 某个 gene 需要从 rejected 恢复为 scored。
- HPA/UniProt/GO-CC 存在强核定位证据，但分类或淘汰判断不确定。
- 报告中 IF/PAE/PPI/PDB 明显有数据但连续两次无法获取。
- 总表更新异常、顶部统计出现空行、分类计数不一致。
- 发现脚本或协议本身互相冲突。
- 需要访问项目路径外的大量文件或做高风险操作。

## 非硬停止情况

以下情况不要问用户，继续自动处理：

- 只是在同一 category 内补全文字、图像、PPI 表。
- IF 只有 thumbnail，但已嵌入并标注。
- PAE 确认不可用，但已写明来源和原因。
- PPI 查询真实返回 0，但已写明 STRING/IntAct/BioGrid/UniProt 查询结果。
- 单个 gene 修复耗时较长，但仍在正常查询。

## 每个 gene 必须完成

- 重新核查 HPA reliability/main/additional。
- 尝试 IF rescue，优先 red_green / blue_red_green。
- 重新核查 AlphaFold/pLDDT/PAE/PDB。
- 重新核查 InterPro/Pfam/domain。
- 独立 PubMed strict/broad，不准只读 Excel。
- 重新核查 STRING + IntAct/BioGrid/UniProt interaction。
- PPI 必须是真表。
- scored 报告补齐完整结构。
- rejected 报告也必须有完整淘汰依据，不能一行。
- 运行 targeted strict。
- 运行禁止词 grep。
- 记录到 log。

## Batch summary log

每个 batch 创建或追加：
`log/claude_autonomous_repair_loop_YYYYMMDD_HHMMSS.md`

记录：

- batch 编号
- 使用的协议
- 输入 audit 路径
- 修复 genes
- scored/rejected/category 改动
- IF embedded 数
- PAE embedded 数
- PPI repaired 数
- PubMed strict/broad 更新数
- targeted strict 结果
- forbidden phrase grep 结果
- full gate 结果
- 修复前 CRITICAL/HIGH 数
- 修复后 CRITICAL/HIGH 数
- 是否触发硬停止
- 下一步协议

## 输出格式

不要每 batch 询问是否继续。

每个 batch 完成后只输出简短进度：

```markdown
Batch N 完成。
- 修复 genes:
- 修复前 CRITICAL/HIGH:
- 修复后 CRITICAL/HIGH:
- gate:
- 下一步:
```

全部停止时输出：

- 总 batch 数
- 总 gene 数
- 已修复 genes
- 仍剩 CRITICAL/HIGH 数
- 触发停止原因
- 最新 audit/log 路径
- 是否需要用户判断
