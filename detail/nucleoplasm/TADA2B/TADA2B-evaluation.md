---
type: protein-evaluation
gene: "TADA2B"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TADA2B 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | TADA2B / MGC21874 |
| 蛋白全称 | Transcriptional adapter 2-beta |
| 蛋白大小 | 420 aa |
| UniProt ID | Q86TJ2 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 420 aa，处于理想范围 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 17 篇，极度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: homeodomain-like_sf, myb_dna-binding, sant, sant/myb, san |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **137/183** |  |
| **归一化总分** |  |  | **74.9/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | N/A | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TADA2B/IF_images/A-431_HPA035770_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TADA2B/IF_images/U-251MG_HPA035770_2.jpg|U-251MG]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 420 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 17 |

**评价**: PubMed 17 篇，极度新颖

**关键文献**:
1. Shalem O et al. (2014). "Genome-scale CRISPR-Cas9 knockout screening in human cells". *Science*. PMID: 24336571
2. Haney MS et al. (2025). "In vivo CRISPR screening identifies SAGA complex members as key regulators of hematopoiesis". *bioRxiv*. PMID: 40475452
3. Shankar A et al. (2026). "In vivo CRISPR screening identifies SAGA complex members as key regulators of hematopoiesis". *Nat Commun*. PMID: 41577693
4. Heinbäck R et al. (2025). "Mapping the intracellular HMGB1 interactome and alterations induced by Toll-like receptor 4 activation". *J Biol Chem*. PMID: 41161382
5. Li H et al. (2023). "Integrative analysis of histone acetyltransferase KAT2A in human cancer". *Cancer Biomark*. PMID: 38007639
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 420 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 19 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TADA2B/TADA2B-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | ADA2-like_ZZ |
| InterPro | Ada2/TADA2 |
| InterPro | Ada2b_C |
| InterPro | Homeodomain-like_sf |
| InterPro | SANT/Myb |
| InterPro | SANT_dom |
| InterPro | TADA2A_B-like_dom |
| InterPro | WH-like_DNA-bd_sf |
| InterPro | Znf_ZZ |
| InterPro | Znf_ZZ_sf |
| Pfam | Myb_DNA-binding |
| Pfam | TADA2A-like_3rd |
| Pfam | Tri-helical_Ada2b_C |
| Pfam | ZZ_ADA2 |
| SMART | SANT |

**染色质调控潜力分析**: 染色质/DNA 结构域: homeodomain-like_sf, myb_dna-binding, sant, sant/myb, sant_dom

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:SAGA complex (GO:0000124, NAS:ComplexPortal)
- C:SAGA-type complex (GO:0070461, IDA:BHF-UCL)
- F:chromatin binding (GO:0003682, IBA:GO_Central)
- P:chromatin remodeling (GO:0006338, IBA:GO_Central)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 19 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
多库结构域一致 (+0.5)
**总计**: +1.5

### 4. 总体评价

**推荐等级**: ****o (4/5)

**核心优势**:
1. 新颖性: PubMed 17 篇，极度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=TADA2B
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173011-TADA2B
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22TADA2B%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q86TJ2
- STRING: https://string-db.org/network/9606.ENSG00000173011
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86TJ2


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[TADA2B-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TADA2B/TADA2B-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000173011-TADA2B/subcellular

![](https://images.proteinatlas.org/35770/2266_E4_134_red_green.jpg)
![](https://images.proteinatlas.org/35770/2266_E4_160_red_green.jpg)
![](https://images.proteinatlas.org/35770/392_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/35770/392_B6_2_red_green.jpg)
![](https://images.proteinatlas.org/35770/393_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/35770/393_B6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
