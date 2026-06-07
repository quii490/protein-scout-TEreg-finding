---
type: protein-evaluation
gene: "FGGY"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, scored]
status: scored
---

## FGGY 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FGGY |
| 蛋白大小 | 551 aa |
| UniProt ID | Q96C11 (FGGY carbohydrate kinase domain-containi) |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FGGY/IF_images/NIH-3T3_1.jpg|NIH 3T3]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FGGY/IF_images/EFO-21_1.jpg|EFO-21]]


### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | x4 | 28 | 暂无数据（HPA IF 图像已本地嵌入。

| 📏 蛋白大小 | 10/10 | x1 | 10 | 551 aa |
| 🆕 研究新颖性 | 10/10 | x5 | 50 | PubMed 18 篇 |
| 🏗️ 三维结构 | 8/10 | x3 | 24 | AlphaFold pLDDT 96.0, v6 |
| 🧬 调控结构域 | 7/10 | x2 | 14 | InterPro 5 个结构域条目 |
| 🔗 PPI 网络 | 4/10 | x3 | 12 | STRING 0 partners |
| ➕ 互证加分 | — | max +3 | +0.5 | 核候选保守蛋白基线 |
| **原始总分** |  |  | **138.5/183** |  |
| **归一化总分** |  |  | **75.7/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA | 暂无数据 | Tier1 |
| UniProt | 暂无数据 | — |

**结论**: 暂无数据（HPA IF 图像已本地嵌入。


#### 3.2 蛋白大小评估
- 551 aa
- 大小适宜性评分：10/10

**评价**: 551 aa 蛋白，适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 18 |
| 新颖性评分 | 10/10 |

**评价**: PubMed 18 篇，属于极度新颖，几乎未被研究。

**关键文献**:
1. Sun Z et al. (2022). "LINE-1 promotes tumorigenicity and exacerbates tumor progression via stimulating metabolism reprogramming in non-small cell lung cancer". *Mol Cancer*. PMID: 35842613
2. Singh C et al. (2017). "Molecular Identification of d-Ribulokinase in Budding Yeast and Mammals". *J Biol Chem*. PMID: 27909055
3. Liu L et al. (2025). "Downregulating FGGY carbohydrate kinase domain containing promotes cell senescence by activating the p53/p21 signaling pathway in colorectal cancer". *Int J Mol Med*. PMID: 40116125
4. Lou S et al. (2024). "Integrative Multi-omics Analysis Identifies Genetic Variants Contributing to Non-syndromic Cleft Lip with or without Cleft Palate". *Chin J Dent Res*. PMID: 38546521
5. Ahmad S et al. (2024). "Genome-wide association study meta-analysis of neurofilament light (NfL) levels in blood reveals novel loci related to neurodegeneration". *Commun Biol*. PMID: 39251807
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 96.0 |
| 有序区域 (pLDDT>70) 占比 | 98.4% |
| pLDDT>90 占比 | 96.0% |
| pLDDT 70-90 占比 | 2.4% |
| pLDDT 50-70 占比 | 0.5% |
| pLDDT<50 占比 | 1.1% |
| AlphaFold 版本 | v6 |
| 可用 PDB 条目 | 查询中 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FGGY/FGGY-PAE.png]]

**评价**: AlphaFold高质量预测（pLDDT=96.0）。有高置信度折叠域，结构可信度高。评分 8/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| Carbohydrate kinase, FGGY | IPR |
| FGGY carbohydrate kinase, pentulose kinase | IPR |
| Carbohydrate kinase FGGY, N-terminal | IPR |
| Carbohydrate kinase FGGY, C-terminal | IPR |
| ATPase, nucleotide binding domain | IPR |

**染色质调控潜力分析**: InterPro 注释了 5 个结构域条目。包含其他结构域类型。评分 7/10。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| 无高置信度互作伙伴 | — | — | — |

**GO-CC 复合体**: 从 UniProt GO 注释提取

**PPI 互证分析**:
- STRING 高置信度 (>0.7) partners: 0 个
- 调控相关比例: 待进一步分析

**评价**: STRING 数据库显示 0 个互作伙伴。评分 4/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT 96.0 | — |
| 结构域 | InterPro | 5 个条目 | — |
| PPI | STRING | 0 partners | — |
| 定位 | HPA / UniProt | 待确认 | — |

**互证加分明细**:
- 进化保守性: 核候选保守蛋白 → +0.5
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (4.0/5)

**核心优势**:
1. 极度新颖，PubMed ≤20 篇
2. AlphaFold 结构质量好 (pLDDT>80)

**风险/不确定性**:
1. 结构可接受
2. '研究数据有限，需更多实验验证'

**下一步建议**:
- [ ] 在 TEreg 系统中检测 FGGY 表达及定位
- [ ] 通过 co-IP/MS 验证 PPI 网络
- [ ] ChIP-seq 检查 FGGY 在 TE 区域的 occupancy

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96C11
- Protein Atlas: https://www.proteinatlas.org/search/FGGY
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96C11
- STRING: https://string-db.org/network/9606.FGGY
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/Q96C11/


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[FGGY-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FGGY/FGGY-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96C11 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR043129;IPR000577;IPR018485;IPR018484;IPR006003; |
| Pfam | PF02782;PF00370; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000172456-FGGY/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MRPS22 | Biogrid | false |
| NSFL1C | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
