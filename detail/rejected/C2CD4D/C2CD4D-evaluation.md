---
type: protein-evaluation
gene: "C2CD4D"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## C2CD4D — REJECTED (数据不可用)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | C2CD4D |
| 数据状态 | 无 harvest packet |
| 评估日期 | 2026-06-03 |

### 2. 淘汰理由

**数据不可用**: 该基因在 harvest_packets 目录中无对应 JSON 文件，无法进行 /180 标准评分。可能原因包括：
- 该基因末被纳入原始 harvest pipeline
- UniProt 中无对应的人类蛋白条目
- 基因符号命名变化

### 3. 后续建议

- [ ] 确认基因符号是否为新命名（检查 HGNC 最新命名规范）
- [ ] 在 UniProt 检索对应的人类蛋白条目
- [ ] 如找到有效条目，重新运行 harvest pipeline 生成数据包

### 4. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/?query=C2CD4D
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C2CD4D
