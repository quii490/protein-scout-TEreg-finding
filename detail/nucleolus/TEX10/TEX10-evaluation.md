---
type: protein-evaluation
gene: "TEX10"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TEX10 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | TEX10 / FLJ20287|bA208F1.2|Ipi1 |
| 蛋白全称 | Testis-expressed protein 10 |
| 蛋白大小 | 929 aa |
| UniProt ID | Q9NXF1 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TEX10/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TEX10/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | **28** | UniProt 核定位，部分细胞质 |
| 蛋白大小 | 8/10 | ×1 | **8** | 929 aa，尚可接受 |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed 42 篇，高度新颖 |
| 三维结构 | 8/10 | ×3 | **24** | 4 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 8 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
|  | **原始总分** |  | **111/183** | **110.0/183** |  |  |  |
|  | **归一化总分** |  | **60.7/100** | **60.1/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus, nucleoplasm, Cytoplasm, Nucleus, nucleolus | 实验证据/预测 |
| GO-CC | GO:0005634 | IEA|ISS |

**结论**: UniProt Nucleus + partial cyto

#### 3.2 蛋白大小评估

**评价**: 929 aa，尚可接受

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 42 |

**评价**: PubMed 42 篇，高度新颖

**关键文献**:
1. Huang J & Tong L (2025). "Molecular insights into the overall architecture of human rixosome". *Nat Commun*. PMID: 40195365
2. Yuan F et al. (2025). "Pluripotency factor Tex10 finetunes Wnt signaling for spermatogenesis and primordial germ cell development". *Nat Commun*. PMID: 39988597
3. Sieper MH et al. (2024). "Scrutinizing the human TEX genes in the context of human male infertility". *Andrology*. PMID: 37594251
4. Finkbeiner E et al. (2011). "SUMO routes ribosome maturation". *Nucleus*. PMID: 22064470
5. Xiang X et al. (2023). "Tex10 interacts with STAT3 to regulate hepatocellular carcinoma growth and metastasis". *Mol Carcinog*. PMID: 37792308
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 929 aa |
| PDB 条数 | 4 |
| 已注释结构域 | 8 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TEX10/TEX10-PAE.png]]

**评价**: 4 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | ARM-like |
| InterPro | ARM-type_fold |
| InterPro | HEAT_type_2 |
| InterPro | Ipi1_N |
| InterPro | TPR_TEX10 |
| Pfam | Ipi1_N |
| Pfam | TPR_TEX10 |
| PROSITE | HEAT_REPEAT |

**染色质调控潜力分析**: 8 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| H1F5 | cross-linking study | 30021884 | — | — |
| KIF28P | cross-linking study | 30021884 | — | — |
| EBI-22312375 | two hybrid array | 32296183 | — | — |
| EBI-22266552 | clash | 23622248 | — | — |
| EBI-21019856 | clash | 23622248 | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:MLL1 complex (GO:0071339, IDA:UniProtKB)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 4 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 8 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
PDB + AlphaFold 结构互证 (+0.5)
多库结构域一致 (+0.5)
**总计**: +2.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 42 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 4 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=TEX10
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136891-TEX10
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22TEX10%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9NXF1
- STRING: https://string-db.org/network/9606.ENSG00000136891
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NXF1


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[TEX10-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/TEX10/TEX10-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000136891-TEX10/subcellular

![](https://images.proteinatlas.org/45434/1177_H4_1_red_green.jpg)
![](https://images.proteinatlas.org/45434/1177_H4_2_red_green.jpg)
![](https://images.proteinatlas.org/45434/625_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/45434/625_D9_2_red_green.jpg)
![](https://images.proteinatlas.org/45434/631_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/45434/631_D9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
