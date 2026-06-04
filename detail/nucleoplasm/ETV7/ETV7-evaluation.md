---
type: protein-evaluation
gene: "ETV7"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ETV7 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ETV7 / TEL-2, TEL2 |
| 蛋白名称 | Transcription factor ETV7 |
| UniProt ID | Q9Y603 |
| 蛋白大小 | 341 aa |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA Chromosome+Nucleoplasm+Nucleoli + UniProt Nucleus + GO chromatin |
| 蛋白大小 | 10/10 | ×1 | 10 | 341 aa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed 62 篇 (51-100) |
| 三维结构 | 8/10 | ×3 | 24 | AF pLDDT=64.8 + PDB:9HK0 |
| 调控结构域 | 9/10 | ×2 | 18 | ETS domain + Pointed domain, 转录因子 |
| PPI 网络 | 6/10 | ×3 = 18 | ETV6 homodimer, BATF2 immune TF |
| 互证加分 | — | max +3 | +1.5 | PDB+ETS域+GO chromatin+多源核定位 |
| **原始总分** |  |  | **127.5/183** |  |
| **归一化总分** |  |  | **69.7/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|------|------|--------|
| TEreg 筛选 | 核评分 6 | Tier1 |
| Protein Atlas (IF) | Chromosome, Mitotic chromosome, Nuclear bodies, Nucleoli, Nucleoplasm | Supported |
| UniProt | Nucleus | Reviewed |
| GO-Cellular Component | Chromatin, Nucleoplasm | IDA |


**HPA IF 图像**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ETV7/IF_images/64555_A_8_4_rna_selected.jpg|HPA IF]]

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ETV7/IF_images/64555_A_9_3_rna_selected.jpg|HPA IF]]

**结论**: 极其丰富的 HPA 核内定位模式（染色体、核仁、核体、核质）。多源高度一致确认核定位。作为 ETS 家族转录因子，染色质/染色体定位是其功能定位。

#### 3.2 蛋白大小评估
**评价**: 341 aa，理想实验范围。

#### 3.3 研究现状
| 指标 | 数值 |
|------|------|
| PubMed 总数 | 62 |
| 主要研究方向 | 造血转录因子, ETS 家族, 白血病 |

**主要研究方向**:
- ETS 家族转录抑制因子
- 造血干细胞调控
- 与 ETV6 (TEL) 相关

**关键文献**:
1. Potter et al. (2000). "TEL2/ETV7 identification". PMID: 10688683
2. Carella et al. (2006). "ETV7 in hematopoiesis". PMID: 17185408
3. Gu et al. (2001). "TEL2 hematopoietic role". PMID: 11282887

**评价**: 研究适中（62篇），以造血系统研究为主。作为转录因子功能明确。

#### 3.4 三维结构分析
| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| 平均 pLDDT | 64.8 |
| 有序区域 (pLDDT>70) 占比 | 43% |
| 可用 PDB 条目 | 9HK0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ETV7/ETV7-PAE.png]]

**评价**: AF 预测中等，1个 PDB 实验结构。ETS domain + Pointed domain 有局部高置信度折叠。

#### 3.5 结构域分析
| 来源 | 结构域 |
|------|--------|
| InterPro | ETS domain (IPR000418) |
| InterPro | Pointed domain (IPR003118) |
| InterPro | SAM/Pointed domain superfamily (IPR013761) |
| Pfam | Ets, SAM_PNT |

**染色质调控潜力分析**: ETS 家族经典 DNA 结合转录因子。ETS domain 识别 GGA(A/T) 核心基序。Pointed (SAM) domain 参与蛋白-蛋白互作和同源/异源二聚化。DNA 结合功能极其明确。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作**:
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| ETV6 | 0.97 | ETS 转录因子(同家族) | 是 |
| BATF2 | 0.87 | bZIP 转录因子 | 是 |
| GBP5 | 0.61 | GTPase | 否 |
| ANKRD22 | 0.57 | 膜蛋白 | 否 |

**已知复合体成员** (GO Cellular Component):
- Chromatin (GO:0000785)
- Nucleoplasm (GO:0005654)

**PPI 互证分析**:
- ETV6 同家族互作: ETS 家族二聚化
- 调控相关比例: 中等 (~30%)

**评价**: PPI 以同家族转录因子为主（ETV6），有 BATF2 免疫转录因子。GO chromatin 注释有 IDA 实验证据。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AF + PDB(9HK0) | ETS + Pointed fold | 一致 |
| 结构域 | InterPro/Pfam | ETS DNA-binding | 一致 |
| PPI | STRING | ETV6 二聚化 | 一致 |
| 定位 | HPA / UniProt / GO | Chromatin/Nucleoplasm/Nucleoli | 一致 |

**互证加分明细**:
- PDB 实验结构 (+0.5)
- ETS 域 + GO chromatin 一致 (+0.5)
- 多源核定位一致 (+0.5)
- **总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: 4 / 5

**核心优势**:
1. 经典 ETS 转录因子，DNA 结合域确认
2. HPA 显示极其丰富的核内定位模式（染色体、核仁、核体）
3. GO chromatin 有 IDA 实验证据
4. ETV6 同家族互作

**风险/不确定性**:
1. 研究热度中等（62篇）
2. 在非造血系统中的功能未知

**下一步建议**:
- [ ] ChIP-seq 检测 ETV7 在非造血细胞中的基因组结合
- [ ] 分析 ETV7 结合基序是否在 TE 区域富集
- [ ] 比较 ETV7 与 ETV6 在 TE 调控中的差异性

### 5. 数据来源
- UniProt: Q9Y603 (https://www.uniprot.org/uniprotkb/Q9Y603)
- AlphaFold: AF-Q9Y603-F1 v6 (https://alphafold.ebi.ac.uk/entry/Q9Y603)
- Protein Atlas: ETV7 (https://www.proteinatlas.org/)
- PubMed: ETV7 (https://pubmed.ncbi.nlm.nih.gov/)
- STRING: ETV7 (https://string-db.org/)
- InterPro: Q9Y603 (https://www.ebi.ac.uk/interpro/)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[ETV7-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ETV7/ETV7-PAE.png]]




