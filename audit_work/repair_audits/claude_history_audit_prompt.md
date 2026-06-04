你是 Claude Code worker。当前任务是 TEreg-finding/protein-interested 项目的“历史评估全量审计与修复”阶段。用户更重视准确度和完整性，速度次要。

工作目录：/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested
可参考 Excel：/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/Final_TE_finding.xlsx

最高优先级规则：
1. 不要手动编辑 protein-finding.md 的表格部分；总表只能通过 rebuild_summary.py 重建。
2. 不要因为 HPA/PAE 确实无数据而失败；但报告必须有显式说明。已有 IF/PAE 文件则必须嵌入且路径存在。
3. 不要凭空补数据。数据缺失时优先查 API/网页；如果确实没有，写清楚“暂无数据/0 条/无注释”和定位依据。
4. 每次修复一类问题后运行 validate_strict.py；最后运行 rebuild_summary.py，然后 validate_strict.py --all --json。
5. 保留 audit_work/ 下的审计记录，说明修了什么、还有什么 warning 或需要人工复核。

已有初始审计结果：
- 约 1969 个报告被 validate_strict.py --all 覆盖。
- 348 个报告有 error，636 个有 warning。
- 主要 error 类型：
  - Scored report has unparseable normalized score
  - IF embed points to missing file
  - No IF image files; report must explicitly state HPA/Protein Atlas IF absence
  - Normalized score does not match formula result
  - Novelty score does not match PubMed expected bucket
  - PPI section does not explicitly cover IntAct/BioGrid, STRING, GO-CC
- 发现 26 个基因重复出现在多个分类目录，需记录并尽量按证据修复；如果不能安全自动决定，列入 manual_review_duplicates.md。

你要执行：
A. 读取 validate_strict.py 和 /private/tmp/protein_audit_all_initial.json，如果 tmp 文件不存在就重新生成：
   python3 validate_strict.py --all --json > audit_work/audit_all_before.json
B. 按 error 类型优先修复历史报告：
   1) broken IF embeds：如果目标文件实际在当前 gene 目录或 rejected/gene/IF_images 中存在，修正 wikilink；如果确实没有图片，则删除断链 embed 并写明确 HPA/Protein Atlas IF 暂无数据/待分析说明，不能留下断链。
   2) normalized score：根据评分表维度、权重和互证加分重算并修正原始总分/归一化总分。若 PubMed bucket 错，先修新颖性分数，再重算总分。
   3) unparseable normalized：修成统一格式，例如 `| **归一化总分** | | | **75.1/100** | |`，并保证 rebuild_summary.py 可解析。
   4) PPI source missing：优先查看本地缓存/现有 JSON/TSV；必要时用 API 查询 IntAct、STRING、UniProt GO-CC。结果为 0 也要明确写入 3.6 PPI 网络，不可省略来源。
   5) No IF image/no explanation：查 HPA/Protein Atlas；有图则下载并嵌入，没有则写明确无数据说明。
C. 修复后运行：
   python3 rebuild_summary.py
   python3 validate_strict.py --all --json > audit_work/audit_all_after.json
D. 生成 audit_work/history_audit_report.md，包含：
   - 修复前后 error/warning 数
   - 修复的文件/问题类型摘要
   - 仍有 error 的基因列表（如果有）
   - warning 分类和是否可接受
   - 需要人工复核的重复/定位可疑/数据源不可确认项
E. 先不要开始 sheet3/sheet4 大规模新评估。只生成候选清单：
   - audit_work/sheet3_research_many_missing.json：Excel 第 3 个工作表 `研究很多` 中尚未评估的 human_symbol
   - audit_work/sheet4_repa_missing.json：Excel 第 4 个工作表 `重新pa一下` 中尚未评估的 human_symbol
   每个 JSON 使用格式：{"genes":[{"gene":"GENE","source_sheet":"研究很多"}]}

完成标准：
- validate_strict.py --all 的 error 尽可能降到 0；如果无法为 0，必须说明每个剩余 error 的原因和下一步。
- protein-finding.md 已通过 rebuild_summary.py 更新。
- audit_work/history_audit_report.md 存在。

请直接执行，不要只给计划。