---
type: protein-evaluation
gene: "PPRC1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PPRC1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PPRC1 / PRC|KIAA0595|MGC74642 |
| 蛋白全称 | Peroxisome proliferator-activated receptor gamma coactivator-related protein 1 |
| 蛋白大小 | 1664 aa |
| UniProt ID | Q5VV67 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 5/10 | ×1 | **5** | 1664 aa, small/large |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 17 篇，极度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 8 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **126/183** |  |
| **归一化总分** |  |  | **68.9/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | GO:0005634 | IBA|IDA|IEA |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PPRC1/IF_images/A-431_HPA038511_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PPRC1/IF_images/U-251MG_HPA038511_2.jpg|U-251MG]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 1664 aa， small/large

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 17 |

**评价**: PubMed 17 篇，极度新颖

**关键文献**:
1. Shi D et al. (2021). "An isocaloric moderately high-fat diet extends lifespan in male rats and Drosophila". *Cell Metab*. PMID: 33440166
2. He X et al. (2012). "Peri-implantation lethality in mice lacking the PGC-1-related coactivator protein". *Dev Dyn*. PMID: 22411706
3. Alkaissi H et al. (2016). "Genome-Wide Association Study to Identify Genes Related to Renal Mercury Concentrations in Mice". *Environ Health Perspect*. PMID: 26942574
4. Tseng C et al. (2024). "Advanced glycation end products promote intervertebral disc degeneration by transactivation of matrix metallopeptidase genes". *Osteoarthritis Cartilage*. PMID: 37717904
5. Zhao S et al. (2022). "[Clinicopathological features of polymorphous low-grade neuroepithelial tumor of the young]". *Zhonghua Bing Li Xue Za Zhi*. PMID: 35785835
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 1664 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 8 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PPRC1/PPRC1-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Nucleotide-bd_a/b_plait_sf |
| InterPro | PGC-1 |
| InterPro | PRC_RRM |
| InterPro | RBD_domain_sf |
| InterPro | RRM_dom |
| Pfam | RRM_1 |
| SMART | RRM |
| PROSITE | RRM |

**染色质调控潜力分析**: 8 个已注释结构域，新颖蛋白基线水平

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
| 结构域 | UniProt/InterPro/Pfam | 8 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
多库结构域一致 (+0.5)
**总计**: +1.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

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
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PPRC1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000148840-PPRC1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PPRC1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q5VV67
- STRING: https://string-db.org/network/9606.ENSG00000148840
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5VV67


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PPRC1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PPRC1/PPRC1-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000148840-PPRC1/subcellular

![](https://images.proteinatlas.org/38511/449_C11_1_red_green.jpg)
![](https://images.proteinatlas.org/38511/449_C11_2_red_green.jpg)
![](https://images.proteinatlas.org/38511/452_C11_1_red_green.jpg)
![](https://images.proteinatlas.org/38511/452_C11_2_red_green.jpg)
![](https://images.proteinatlas.org/38511/455_C11_1_red_green.jpg)
![](https://images.proteinatlas.org/38511/455_C11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
