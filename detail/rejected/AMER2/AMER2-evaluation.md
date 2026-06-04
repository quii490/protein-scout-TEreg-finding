---
type: protein-evaluation
gene: "AMER2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## AMER2 -- 评估报告（REJECTED）

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | AMER2 |
| 评估日期 | 2026-06-03 |
| 数据状态 | harvest packet缺失 |

### 2. 拒绝原因

**核心原因: 数据不可用。AMER2 的harvest packet JSON文件在 protein_data/harvest_packets/ 目录中不存在，无法从自动化pipeline获取UniProt、AlphaFold、PubMed、STRING、IntAct、HPA等必需数据库信息。**


**备注**: AMER2 (APC membrane recruitment protein 2) 是Wnt信号通路的膜招募蛋白，已知功能定位于质膜和细胞质，参与β-catenin降解复合体的膜招募。该蛋白不太可能具有核定位功能，理论上不适合作为核蛋白研究目标。


### 3. 数据获取状态

| 数据库 | 状态 | 说明 |
|---|---|---|
| UniProt | 不可用 | harvest packet缺失，无accession、序列长度、功能注释、亚细胞定位 |
| AlphaFold | 不可用 | harvest packet缺失，无pLDDT统计、PAE图像、PDB文件 |
| PubMed | 不可用 | harvest packet缺失，无文献计数、关键论文列表 |
| STRING | 不可用 | harvest packet缺失，无蛋白互作网络数据 |
| IntAct | 不可用 | harvest packet缺失，无实验验证互作记录 |
| HPA | 不可用 | harvest packet缺失，无免疫荧光定位、可靠性评分 |

### 4. 影响分析

缺乏harvest packet意味着无法进行以下六维核心评估:

| 评估维度 | 受影响的数据点 | 影响程度 |
|---|---|---|
| 核定位特异性 | HPA IF定位、UniProt Subcellular Location、GO Cellular Component | 完全无法评估 |
| 蛋白大小 | 氨基酸序列长度、分子量 | 完全无法评估 |
| 研究新颖性 | PubMed strict/broad文献计数 | 完全无法评估 |
| 三维结构 | AlphaFold pLDDT、PDB实验结构 | 完全无法评估 |
| 调控结构域 | InterPro/Pfam结构域注释 | 完全无法评估 |
| PPI网络 | STRING/IntAct/UniProt互作数据 | 完全无法评估 |

### 5. 可能原因分析

1. **基因名问题**: 基因符号可能不是当前HGNC官方符号，或存在别名未被识别
2. **数据库覆盖**: 该基因产物可能未被UniProt review（如TrEMBL条目），或为predicted protein
3. **Pipeline覆盖**: harvest pipeline可能未处理该基因（如批次遗漏、API限制）
4. **产物类型**: 该基因可能为假基因（pseudogene）、非编码RNA、或未充分注释的阅读框
5. **文件清理**: packet文件可能被误删除或移动到其他位置

### 6. 补救建议

1. 确认 AMER2 的当前HGNC官方符号，如有变更重新运行harvest
2. 手动检查 UniProt (https://www.uniprot.org) 和 GeneCards (https://www.genecards.org) 确认基因存在性
3. 如基因确实存在且有研究价值，手动创建harvest packet或使用交互式工具逐数据库查询
4. 如果确认该基因无数据库记录，将其标记为不适合当前研究目标
5. 对于已知功能定位于膜/胞质的基因（如AMER家族），可基于文献知识直接判定为不符合核蛋白标准

### 7. 评估结论

AMER2 因harvest packet数据缺失，无法完成标准六维蛋白评估。在获得完整数据之前，**维持拒绝状态**。如后续补充packet数据或确认该基因的数据库记录状态，可重新进行完整评估。

![[Projects/TEreg-finding/protein-interested/detail/rejected/AMER2/AMER2-PAE.png]]
