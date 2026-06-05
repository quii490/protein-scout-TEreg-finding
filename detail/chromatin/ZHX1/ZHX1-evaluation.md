---
type: protein-evaluation
gene: "ZHX1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ZHX1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | ZHX1 / -- |
| 蛋白全称 | Zinc fingers and homeoboxes protein 1 |
| 蛋白大小 | 873 aa |
| UniProt ID | Q9UKY1 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/ZHX1/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/ZHX1/IF_images/PC-3_1.jpg|PC-3]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 8/10 | ×1 | **8** | 873 aa，尚可接受 |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed 43 篇，高度新颖 |
| 三维结构 | 8/10 | ×3 | **24** | 4 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: homeobox_2, homeodomain, homeodomain-like_sf, homez_homeo |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
|  | **原始总分** |  | **121/183** | **120.0/183** |  |  |  |
|  | **归一化总分** |  | **66.1/100** | **65.6/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | GO:0005634 | IEA |

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 873 aa，尚可接受

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 43 |

**评价**: PubMed 43 篇，高度新颖

**关键文献**:
1. Kwon RJ et al. (2017). "Roles of zinc-fingers and homeoboxes 1 during the proliferation, migration, and invasion of glioblastoma cells". *Tumour Biol*. PMID: 28351300
2. Yang Y et al. (2024). "Yersinia ruckeri Infection and Enteric Redmouth Disease among Endangered Chinese Sturgeons, China, 2022". *Emerg Infect Dis*. PMID: 38781928
3. Macé C et al. (2020). "The zinc fingers and homeoboxes 2 protein ZHX2 and its interacting proteins regulate upstream pathways in podocyte diseases". *Kidney Int*. PMID: 32059999
4. Chugh SS & Clement LC (2023). ""Idiopathic" minimal change nephrotic syndrome: a podocyte mystery nears the end". *Am J Physiol Renal Physiol*. PMID: 37795536
5. Bird LE et al. (2010). "Novel structural features in two ZHX homeodomains derived from a systematic study of single and multiple domains". *BMC Struct Biol*. PMID: 20509910
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 873 aa |
| PDB 条数 | 4 |
| 已注释结构域 | 13 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/ZHX1/ZHX1-PAE.png]]

**评价**: 4 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | HD |
| InterPro | Homeodomain-like_sf |
| InterPro | Homez_homeobox_dom |
| InterPro | ZHX_Znf_C2H2 |
| InterPro | Znf_C2H2_sf |
| InterPro | Znf_C2H2_type |
| Pfam | Homeodomain |
| Pfam | Homez |
| Pfam | zf_C2H2_ZHX |
| SMART | HOX |
| SMART | ZnF_C2H2 |
| PROSITE | HOMEOBOX_2 |
| PROSITE | ZINC_FINGER_C2H2_2 |

**染色质调控潜力分析**: 染色质/DNA 结构域: homeobox_2, homeodomain, homeodomain-like_sf, homez_homeobox_dom, zf_c2h2_zhx

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:chromatin (GO:0000785, ISA:NTNU_SB)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 4 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 13 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
PDB + AlphaFold 结构互证 (+0.5)
多库结构域一致 (+0.5)
**总计**: +2.0

### 4. 总体评价

**推荐等级**: ****o (4/5)

**核心优势**:
1. 新颖性: PubMed 43 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 4 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=ZHX1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165156-ZHX1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22ZHX1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9UKY1
- STRING: https://string-db.org/network/9606.ENSG00000165156
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UKY1


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[ZHX1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/ZHX1/ZHX1-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000165156-ZHX1/subcellular

![](https://images.proteinatlas.org/55357/875_F7_2_red_green.jpg)
![](https://images.proteinatlas.org/55357/875_F7_3_red_green.jpg)
![](https://images.proteinatlas.org/55357/883_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/55357/883_F7_2_red_green.jpg)
![](https://images.proteinatlas.org/55357/886_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/55357/886_A3_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
