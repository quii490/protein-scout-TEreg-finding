---
type: protein-evaluation
gene: "CCDC137"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC137 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC137 / Coiled-coil domain-containing protein 137 |
| 蛋白大小 | 289 aa / 33.2 kDa |
| UniProt ID | Q6PK04 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CCDC137/IF_images/CACO-2_1.jpg|CACO-2]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CCDC137/IF_images/PC-3_1.jpg|PC-3]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | Chromosome |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 289 aa / 33.2 kDa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 40 篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.0，PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026680 - CCDC137 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 20 partners, IntAct 229 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** |  |  | **121/183** |  |
| **归一化总分** |  |  | **66.1/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Chromosome | Swiss-Prot/TrEMBL |
| Protein Atlas (IF) | 暂无数据 | 暂无 HPA IF 数据 |

暂无数据（HPA IF 图像已本地嵌入。


**结论**: 主要核定位，伴部分胞质信号，HPA 暂无 HPA IF 数据。

#### 3.2 蛋白大小评估

**评价**: 大小适中，适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 40 |
| 研究方向 | 待补充关键文献摘要 |

**评价**: 非常新颖，仅有少数基础研究。

**关键文献**:
1. Zhang H et al. (2025). "CCDC137 knockdown suppresses bladder cancer progression by downregulating SCD". *J Transl Med*. PMID: 40993629
2. Tao S et al. (2023). "RNA-binding protein CCDC137 activates AKT signaling and promotes hepatocellular carcinoma through a novel non-canonical role of DGCR8 in mRNA localization". *J Exp Clin Cancer Res*. PMID: 37542342
3. Nisson KA et al. (2025). "HIV Vpr activates a nucleolar-specific ATR pathway to degrade the nucleolar stress sensor CCDC137". *Nucleic Acids Res*. PMID: 40530693
4. Xu L et al. (2025). "Disrupting CCDC137-mediated LZTS2 and β-TrCP interaction in the nucleus inhibits hepatocellular carcinoma development via β-catenin and AKT". *Cell Death Differ*. PMID: 38918619
5. Xu Z et al. (2025). "CCDC137/DGCR8 axis promotes aerobic glycolysis in hepatocellular carcinoma via activation of the AKT/mTOR signaling pathway". *Eur J Med Res*. PMID: 41029756
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.0 |
| 高置信度残基 (pLDDT>90) 占比 | 28.4% |
| 置信残基 (pLDDT 70-90) 占比 | 28.7% |
| 有序区域 (pLDDT>70) 占比 | 57.1% |
| 可用 PDB 条目 | 无 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CCDC137/CCDC137-PAE.png]]

**评价**: AlphaFold 中等质量（pLDDT=74.0，有序区 57.1%）。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026680 - CCDC137 |

**染色质调控潜力分析**: 存在注释结构域：InterPro: IPR026680 - CCDC137...。新颖蛋白基线不扣分。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| NOL12 | 0.742 | — | — |
| TMEM69 | 0.652 | — | — |
| DDX27 | 0.635 | — | — |
| ZC3H10 | 0.63 | — | — |
| NPM1 | 0.622 | — | — |
| RPL8 | 0.615 | — | — |
| NIFK | 0.601 | — | — |
| CBLN3 | 0.573 | — | — |
| GPATCH4 | 0.558 | — | — |
| RRP8 | 0.546 | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-712794|uniprotkb:O76079|uniprotkb:Q96L83|uniprotkb:Q9BTI8|uniprotkb:C9J8H9|uniprotkb:F8W7V3|uniprotkb:Q6IBB3|intact:EBI-11047094|ensembl:ENSP00000292475.4 | — | — | — | — |
| intact:EBI-716157|uniprotkb:Q4GX05|uniprotkb:Q6PGR3|uniprotkb:Q86SV1|uniprotkb:B2R7N0|uniprotkb:D3DX47|uniprotkb:A0A0C4DGP3|ensembl:ENSP00000381425.4 | — | — | — | — |
| intact:EBI-6381269|uniprotkb:Q13583|uniprotkb:Q4F970|uniprotkb:Q562F5|uniprotkb:Q9UM62|ensembl:ENSP00000359119.3 | — | — | — | — |
| intact:EBI-356625|uniprotkb:P08227|uniprotkb:P10660|uniprotkb:Q4VBY7|uniprotkb:Q8N6Z7|ensembl:ENSP00000369757.4 | — | — | — | — |
| intact:EBI-20625235|uniprotkb:H9A910 | — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- 无 GO-CC 注释

**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 20
- 仅 IntAct 实验: 229
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 20 个预测互作，IntAct 229 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.0 + PDB: 无 | pLDDT=74.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Chromosome | 待确认 |
| PPI | STRING + IntAct | 20 + 229 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CCDC137 — Coiled-coil domain-containing protein 137，非常新颖，仅有少数基础研究。
2. 蛋白大小289 aa，大小适中，适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 40 篇，研究基础有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新 5 篇关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6PK04
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC137
- AlphaFold: https://alphafold.ebi.ac.uk/entry/CCDC137


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[CCDC137-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CCDC137/CCDC137-PAE.png]]


