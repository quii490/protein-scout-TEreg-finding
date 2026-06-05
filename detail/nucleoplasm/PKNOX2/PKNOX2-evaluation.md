---
type: protein-evaluation
gene: "PKNOX2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PKNOX2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PKNOX2 / -- |
| 蛋白全称 | Homeobox protein PKNOX2 |
| 蛋白大小 | 472 aa |
| UniProt ID | Q96KN3 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 472 aa，处于理想范围 |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed 55 篇，中等研究热度 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: homeobox_2, homeobox_kn, homeodomain-like_sf, tale_homeob |
| PPI 网络 | 4/10 | ×3 | **12** | STRING 15 个互作伙伴，调控相关性低 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **123/183** |  |
| **归一化总分** |  |  | **67.2/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | N/A | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PKNOX2/IF_images/AF22_HPA028867_1.jpg|AF22]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PKNOX2/IF_images/Rh30_HPA028867_2.jpg|Rh30]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 472 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 55 |

**评价**: PubMed 55 篇，中等研究热度

**关键文献**:
1. Chen L et al. (2024). "PBX/Knotted 1 homeobox-2 (PKNOX2) is a novel regulator of myocardial fibrosis". *Signal Transduct Target Ther*. PMID: 38644381
2. Zhang L et al. (2019). "PKNOX2 suppresses gastric cancer through the transcriptional activation of IGFBP5 and p53". *Oncogene*. PMID: 30745575
3. Nordeidet AN et al. (2023). "Exploring shared genetics between maximal oxygen uptake and disease: the HUNT study". *Physiol Genomics*. PMID: 37575066
4. Trigila AP et al. (2023). "Accelerated Evolution Analysis Uncovers PKNOX2 as a Key Transcription Factor in the Mammalian Cochlea". *Mol Biol Evol*. PMID: 37247388
5. Miyake Y et al. (2021). "PKNOX2 regulates myofibroblast functions and tubular cell survival during kidney fibrosis". *Biochem Biophys Res Commun*. PMID: 34311199
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 472 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 9 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PKNOX2/PKNOX2-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | HD |
| InterPro | Homeodomain-like_sf |
| InterPro | KN_HD |
| InterPro | PKNOX/Meis_N |
| InterPro | TALE_homeobox |
| Pfam | Homeobox_KN |
| Pfam | Meis_PKNOX_N |
| SMART | HOX |
| PROSITE | HOMEOBOX_2 |

**染色质调控潜力分析**: 染色质/DNA 结构域: homeobox_2, homeobox_kn, homeodomain-like_sf, tale_homeobox

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|
| PBX1 | 0 |  | no |
| DDX25 | 0 |  | no |
| HYLS1 | 0 |  | no |
| HOXB1 | 0 |  | no |
| PBX2 | 0 |  | no |
| HOXB2 | 0 |  | no |
| PBX3 | 0 |  | no |
| PBX4 | 0 |  | no |
| LMX1B | 0 |  | no |
| C5orf24 | 0 |  | no |

**已知复合体成员** (GO-CC):

--

**评价**: STRING 15 个互作伙伴，调控相关性低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 9 个 | 多库一致 |
| PPI 网络 | STRING | 15 个 | 单一来源 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
多库结构域一致 (+0.5)
**总计**: +1.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 55 篇，中等研究热度
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PKNOX2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165495-PKNOX2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PKNOX2%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q96KN3
- STRING: https://string-db.org/network/9606.ENSG00000165495
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96KN3


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PKNOX2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PKNOX2/PKNOX2-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000165495-PKNOX2/subcellular

![](https://images.proteinatlas.org/28867/1609_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/28867/1609_C4_3_red_green.jpg)
![](https://images.proteinatlas.org/28867/1684_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/28867/1684_C12_3_red_green.jpg)
![](https://images.proteinatlas.org/28867/1783_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/28867/1783_A3_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
