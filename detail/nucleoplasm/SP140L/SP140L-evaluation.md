---
type: protein-evaluation
gene: "SP140L"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SP140L 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | SP140L / -- |
| 蛋白全称 | Nuclear body protein SP140-like protein |
| 蛋白大小 | 580 aa |
| UniProt ID | Q9H930 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | **16** | Nuclear + cyto, no preference |
| 蛋白大小 | 10/10 | ×1 | **10** | 580 aa，处于理想范围 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 9 篇，极度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: bromodomain, bromodomain-like_sf, bromodomain_2, phd, san |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+0.5** | 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **120.5/183** |  |
| **归一化总分** |  |  | **65.8/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt |  | 实验证据/预测 |
| GO-CC | GO:0005634 | IBA|IEA |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SP140L/IF_images/A-431_HPA055864_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SP140L/IF_images/HeLa_HPA055864_2.jpg|HeLa]]

**结论**: Nuclear + cyto, no preference

#### 3.2 蛋白大小评估

**评价**: 580 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 9 |

**评价**: PubMed 9 篇，极度新颖

**关键文献**:
1. Jaehnig EJ et al. (2025). "Proteogenomic analysis of the CALGB 40601 (Alliance) HER2+ breast cancer neoadjuvant trial reveals resistance biomarkers". *Cell Rep Med*. PMID: 40480221
2. Cable JM et al. (2025). "EBNA2 and EBNA-LP: The Earliest Viral Latency Proteins". *Curr Top Microbiol Immunol*. PMID: 41329188
3. Tao T et al. (2025). "Identification of Crosstalk Genes Between Primary Sjögren's Syndrome and Primary Biliary Cirrhosis by Transcriptome Analysis". *Dig Dis Sci*. PMID: 40199818
4. Cable JM et al. (2025). "Sp140L functions as a herpesvirus restriction factor suppressing viral transcription and activating interferon-stimulated genes". *Proc Natl Acad Sci U S A*. PMID: 40526717
5. Fraschilla I & Jeffrey KL (2020). "The Speckled Protein (SP) Family: Immunity's Chromatin Readers". *Trends Immunol*. PMID: 32386862
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 580 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 24 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SP140L/SP140L-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Bromodomain |
| InterPro | Bromodomain-like_sf |
| InterPro | HSR_dom |
| InterPro | SAND-like_dom_sf |
| InterPro | SAND_dom |
| InterPro | Sp110/Sp140/Sp140L-like |
| InterPro | Sp140_Bromo |
| InterPro | Zinc_finger_PHD-type_CS |
| InterPro | Znf_FYVE_PHD |
| InterPro | Znf_PHD |
| InterPro | Znf_PHD-finger |
| InterPro | Znf_RING/FYVE/PHD |
| Pfam | Bromodomain |
| Pfam | HSR |
| Pfam | PHD |

**染色质调控潜力分析**: 染色质/DNA 结构域: bromodomain, bromodomain-like_sf, bromodomain_2, phd, sand

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
| 结构域 | UniProt/InterPro/Pfam | 24 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | Partially consistent |

**互证加分明细**:
多库结构域一致 (+0.5)
**总计**: +0.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 9 篇，极度新颖
2. 核定位: needs confirmation

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SP140L
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185404-SP140L
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SP140L%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9H930
- STRING: https://string-db.org/network/9606.ENSG00000185404
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H930


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[SP140L-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SP140L/SP140L-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000185404-SP140L/subcellular

![](https://images.proteinatlas.org/55864/1050_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/55864/1050_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/55864/893_G10_1_red_green.jpg)
![](https://images.proteinatlas.org/55864/893_G10_2_red_green.jpg)
![](https://images.proteinatlas.org/55864/895_G10_1_red_green.jpg)
![](https://images.proteinatlas.org/55864/895_G10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
