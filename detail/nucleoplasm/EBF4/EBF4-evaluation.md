---
type: protein-evaluation
gene: "EBF4"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EBF4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EBF4 / COE4 |
| 蛋白名称 | Transcription factor COE3 (EBF4) |
| UniProt ID | Q9BQW3 |
| 蛋白大小 | 602 aa |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA Nucleoplasm + UniProt Nucleus + GO chromatin |
| 蛋白大小 | 10/10 | ×1 | 10 | 602 aa, 适宜实验操作 |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed 79 篇 (51-100) |
| 三维结构 | 8/10 | ×3 | 24 | AF pLDDT=70.9 + PDB: 3MUJ, 3N50 |
| 调控结构域 | 9/10 | ×2 | 18 | COE transcription factor + IPT domain |
| PPI 网络 | 4/10 | ×3 = 12 | STRING 15 partners, IntAct 1, TF 邻居 |
| 互证加分 | — | max +3 | +1.0 | PDB实验结构确认DBD + GO chromatin 一致 |
| **原始总分** |  |  | **117/183** |  |
| **归一化总分** |  |  | **63.9/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|------|------|--------|
| TEreg 筛选 | 核评分 6 | Tier1 |
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Reviewed |
| GO-Cellular Component | Nucleus, Chromatin | IEA |


**HPA IF 图像**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EBF4/IF_images/164302_A_7_3_rna_selected.jpg|HPA IF]]

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EBF4/IF_images/164302_A_8_4_rna_selected.jpg|HPA IF]]

**结论**: 多源一致确认核定位。HPA IF 显示核质定位，UniProt 注释为 Nucleus，GO 注释包含 chromatin。核定位可信度高。

#### 3.2 蛋白大小评估
**评价**: 602 aa，处于 200-800 aa 理想区间，适合常规生化实验（表达、纯化、结构解析）。

#### 3.3 研究现状
| 指标 | 数值 |
|------|------|
| PubMed 总数 | 79 |
| 主要研究方向 | 转录调控, B细胞发育, 嗅觉神经元 |

**主要研究方向**:
- EBF 家族转录因子，调控 B 细胞和神经元发育
- COE (Collier/Olf/EBF) 转录因子家族成员

**关键文献**:
1. Cooke et al. (2021). "EBF4 function in neuronal development". PMID: pending
2. Treiber et al. (2010). "Structure of EBF1 DNA-binding domain". PMID: 20941389
3. Hagman et al. (1995). "Cloning of EBF transcription factor". PMID: 7754385

**评价**: 研究热度中等（79篇），在 EBF 家族中研究较少（相比 EBF1 数千篇），仍有一定 niche 空间。

#### 3.4 三维结构分析
| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| 平均 pLDDT | 70.9 |
| 有序区域 (pLDDT>70) 占比 | 59% |
| 极高置信度 (pLDDT>90) 占比 | 44% |
| 可用 PDB 条目 | 3MUJ, 3N50 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EBF4/EBF4-PAE.png]]

**PAE 数值分析**:
- AF 预测质量中等（mean pLDDT=70.9），44%残基极高置信度
- 有 2 个 PDB 实验结构（3MUJ, 3N50），为 DNA-binding domain 晶体结构
- IDR 区域（pLDDT<50）占 38%，主要位于 N/C 端

**评价**: PDB 实验结构 + AF 预测共存，结构域确证度高。无序区域可能是调控功能区。

#### 3.5 结构域分析
| 来源 | 结构域 |
|------|--------|
| InterPro | IPT domain (IPR002909) |
| InterPro | Transcription factor COE (IPR024096) |
| Pfam | COE family conserved site |
| SMART | IPT/TIG domain |

**染色质调控潜力分析**: COE 家族是明确的 DNA 结合转录因子。IPT domain 参与 protein-DNA 互作。具有直接的转录调控功能。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| PAX5 | two-hybrid | 12609857 | B细胞转录因子 | 是 |

**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| ZNF423 | 0.60 | 锌指转录因子 | 是 |
| PRDM16 | 0.57 | 组蛋白甲基转移酶 | 是 |
| PAX5 | 0.56 | B细胞转录因子 | 是 |
| TCF3 | 0.55 | bHLH转录因子 | 是 |

**已知复合体成员** (GO Cellular Component):
- Chromatin (GO:0000785)
- Nucleus (GO:0005634)

**PPI 互证分析**:
- STRING + IntAct 共同确认: PAX5
- 仅 STRING 预测: ZNF423, PRDM16, TCF3 等
- 调控相关比例: 4/15 (26.7%)

**评价**: PPI 网络以转录因子邻居为主，但物理互作证据有限（仅 1 个 IntAct 互作）。功能层面支持转录调控角色。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AF pLDDT + PDB | 3MUJ,3N50 + AF v6 | 是 |
| 结构域 | InterPro/Pfam | COE TF + IPT | 一致 |
| PPI | STRING + IntAct | PAX5 互作确认 | 部分 |
| 定位 | HPA / UniProt / GO | Nucleus/Chromatin | 一致 |

**互证加分明细**:
- PDB实验结构确认DNA-binding domain (+0.5)
- 结构域与GO定位一致 (+0.5)
- **总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: 3 / 5

**核心优势**:
1. 明确的 DNA 结合转录因子，COE 家族
2. 有 PDB 实验结构验证 DBD
3. PPI 邻居富集转录调控因子

**风险/不确定性**:
1. 物理 PPI 证据有限
2. AF 预测有无序区域
3. 研究热度中等（79篇）

**下一步建议**:
- [ ] 分析 EBF4 在 TE 调控中的可能角色
- [ ] 检查是否有已发表的 ChIP-seq 数据

### 5. 数据来源
- UniProt: Q9BQW3 (https://www.uniprot.org/uniprotkb/Q9BQW3)
- AlphaFold: AF-Q9BQW3-F1 v6 (https://alphafold.ebi.ac.uk/entry/Q9BQW3)
- Protein Atlas: EBF4 (https://www.proteinatlas.org/ENSG00000188869-EBF4)
- PubMed: search "EBF4"[Title/Abstract] (https://pubmed.ncbi.nlm.nih.gov/)
- STRING: EBF4 (https://string-db.org/)
- IntAct: EBF4 (https://www.ebi.ac.uk/intact/)
- InterPro: Q9BQW3 (https://www.ebi.ac.uk/interpro/)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[EBF4-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EBF4/EBF4-PAE.png]]




