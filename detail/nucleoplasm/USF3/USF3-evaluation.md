---
type: protein-evaluation
gene: "USF3"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## USF3 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | USF3 / -- |
| 蛋白全称 | Basic helix-loop-helix domain-containing protein USF3 |
| 蛋白大小 | 2245 aa |
| UniProt ID | Q68DE3 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 2/10 | ×1 | **2** | 2245 aa, too extreme |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 11 篇，极度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: bhlh, bhlh_dom, hlh, hlh_dna-bd_sf, usf3_bhlh |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **129/183** |  |
| **归一化总分** |  |  | **70.5/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | N/A | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/USF3/IF_images/A-431_HPA029243_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/USF3/IF_images/U-251MG_HPA029245_2.jpg|U-251MG]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 2245 aa， too extreme

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 11 |

**评价**: PubMed 11 篇，极度新颖

**关键文献**:
1. Gralak AJ et al. (2024). "Identification of methylation-sensitive human transcription factors using meSMiLE-seq". *bioRxiv*. PMID: 39605503
2. Ye W et al. (2021). "USF3 modulates osteoporosis risk by targeting WNT16, RANKL, RUNX2, and two GWAS lead SNPs rs2908007 and rs4531631". *Hum Mutat*. PMID: 33058301
3. Liu X et al. (2023). "Systematic analysis reveals distinct roles of USF family proteins in various cancer types". *Int J Biol Markers*. PMID: 37846061
4. Wang Y et al. (2020). "Osteoporosis genome-wide association study variant c.3781 C>A is regulated by a novel anti-osteogenic factor miR-345-5p". *Hum Mutat*. PMID: 31883164
5. Wang X et al. (2025). "Modulation of γδ T cells by USF3: Implications for liver fibrosis and immune regulation". *Int Immunopharmacol*. PMID: 39870010
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 2245 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 7 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/USF3/USF3-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | bHLH_dom |
| InterPro | EMT_regulator |
| InterPro | HLH_DNA-bd_sf |
| InterPro | USF3_bHLH |
| Pfam | HLH |
| SMART | HLH |
| PROSITE | BHLH |

**染色质调控潜力分析**: 染色质/DNA 结构域: bhlh, bhlh_dom, hlh, hlh_dna-bd_sf, usf3_bhlh

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

--

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 7 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
多库结构域一致 (+0.5)
**总计**: +1.5

### 4. 总体评价

**推荐等级**: ****o (4/5)

**核心优势**:
1. 新颖性: PubMed 11 篇，极度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=USF3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000176542-USF3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22USF3%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q68DE3
- STRING: https://string-db.org/network/9606.ENSG00000176542
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q68DE3


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[USF3-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/USF3/USF3-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000176542-USF3/subcellular

![](https://images.proteinatlas.org/29243/271_E9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29243/271_E9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/29245/270_D7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29245/270_D7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/29245/271_D7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29245/271_D7_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q68DE3 |
| SMART | SM00353; |
| UniProt Domain [FT] | DOMAIN 18..69; /note="bHLH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00981" |
| InterPro | IPR011598;IPR053252;IPR036638;IPR048064; |
| Pfam | PF00010; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000176542-USF3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SDC2 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
