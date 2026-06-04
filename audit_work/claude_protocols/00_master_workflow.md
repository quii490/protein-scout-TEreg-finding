# 00 总控流程：Protein-Scout Master Workflow

你是 Claude Code 中的 protein-scout 中层主 agent。你的任务是根据当前项目状态选择下一步协议，不要一次性执行所有协议。

## 路径

项目路径：
`/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested`

协议目录：
`audit_work/claude_protocols`

## 目标

最终目标：

- 所有 scored 报告完整、无占位、证据可追溯。
- 所有 rejected 报告有充分淘汰理由，且无明显错杀。
- 所有可得 IF/PAE/PPI/PDB 数据都被正确获取、嵌入或解释。
- `protein-finding.md` 与 detail 报告一致。
- 后续新蛋白评估沿用同一严格流程。

## 决策顺序

按顺序检查并决定下一步：

1. 如果不存在最新 `audit_work/broken_report_audit_*.tsv`，或者该 audit 早于最近一次报告修改：  
   执行 `01_repair_incomplete_reports.md` 的“生成/更新 audit”阶段。

2. 如果最新 broken report audit 中存在 `CRITICAL` 或 `HIGH`：  
   执行 `01_repair_incomplete_reports.md`，每批最多 10 个。

3. 如果不存在最新 `audit_work/data_absence_mismatch_audit_*.tsv`，或者它早于最近一次修复：  
   执行 `02_check_data_absence_mismatch.md`。

4. 如果最新 data absence mismatch audit 中存在 `HIGH`：  
   执行 `03_repair_false_absence.md`，每批最多 10 个。

5. 如果报告中存在“IF 图像已存在/已嵌入，但仍写 Pending/暂无数据/IF unavailable”的矛盾：  
   执行 `07_repair_hpa_if_consistency.md`。

6. 如果不存在最新 `audit_work/false_rejection_candidates_*.tsv`，或者它早于最近一次修复：  
   执行 `04_recheck_false_rejections.md` 的 audit 阶段。

7. 如果最新 false rejection audit 中存在 `HIGH`：  
   执行 `04_recheck_false_rejections.md`，每批最多 10 个。

8. 只有当：
   - broken report audit 无 CRITICAL/HIGH
   - mismatch audit 无 HIGH
   - HPA/IF 语义一致性 audit 无 HIGH
   - false rejection audit 无 HIGH
   - `python3 protein_gate.py --all` 为 `Errors: 0`

   才能执行 `05_continue_new_proteins.md`。

## 禁止

- 禁止越过 audit 直接大规模修复。
- 禁止一次执行多个专项协议。
- 禁止继续新蛋白，除非所有修复队列清空或用户明确要求临时跳过。
- 禁止只因为 `protein_gate.py --all` 通过就认为质量合格。

## 输出

只输出：

- 当前选择的下一步协议
- 选择理由
- 需要执行的文档路径
- 如果无法判断，列出缺失的 audit 文件或 gate 结果
