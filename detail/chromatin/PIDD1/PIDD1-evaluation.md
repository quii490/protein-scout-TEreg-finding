---
type: protein-evaluation
gene: "PIDD1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PIDD1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PIDD1 / MGC16925|DKFZp434D229 |
| 蛋白全称 | p53-induced death domain-containing protein 1 |
| 蛋白大小 | 910 aa |
| UniProt ID | Q9HB75 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/PIDD1/IF_images/NIH-3T3_1.jpg|NIH 3T3]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/PIDD1/IF_images/HEK293_1.jpg|HEK293]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | **16** | Nuclear + cyto, no preference |
| 蛋白大小 | 8/10 | ×1 | **8** | 910 aa，尚可接受 |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed 44 篇，高度新颖 |
| 三维结构 | 8/10 | ×3 | **24** | 1 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 18 个已注释结构域 |
| PPI 网络 | 4/10 | ×3 | **12** | STRING 15 个互作伙伴，调控相关性低 |
| 互证加分 | -- | -- | **+1.0** | PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
|  | **原始总分** |  | **104.5/183** | **104.0/183** |  |  |
|  | **归一化总分** |  | **57.1/100** | **56.8/100** |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Cytoplasm, Nucleus | 实验证据/预测 |
| GO-CC | GO:0005634 | IDA|IEA |

**结论**: Nuclear + cyto, no preference

#### 3.2 蛋白大小评估

**评价**: 910 aa，尚可接受

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 44 |

**关键文献**:
1. Zhang et al. (2025). "Dysregulation of mTOR signalling is a converging mechanism in lissencephaly.". *Nature*. PMID: 39743596
2. Rizzotto et al. (2024). "Caspase-2 kills cells with extra centrosomes.". *Sci Adv*. PMID: 39475598
3. Shah et al. (2024). "Stepwise phosphorylation and SUMOylation of PIDD1 drive PIDDosome assembly in response to DNA repair failure.". *Nat Commun*. PMID: 39448602
4. Miller et al. (2025). "Unraveling ADHD: genes, co-occurring traits, and developmental dynamics.". *Life Sci Alliance*. PMID: 40000109
5. Weiler et al. (2022). "PIDD1 in cell cycle control, sterile inflammation and cell death.". *Biochem Soc Trans*. PMID: 35343572
**评价**: PubMed 44 篇，高度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 910 aa |
| PDB 条数 | 1 |
| 已注释结构域 | 18 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/PIDD1/PIDD1-PAE.png]]

**评价**: 1 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | DEATH-like_dom_sf |
| InterPro | Death_dom |
| InterPro | Leu-rich_rpt |
| InterPro | Leu-rich_rpt_typical-subtyp |
| InterPro | LRR_dom_sf |
| InterPro | LRR_domain-containing |
| InterPro | Peptidase_S68_pidd |
| InterPro | ZU5_dom |
| Pfam | Death |
| Pfam | LRR_8 |
| Pfam | Peptidase_S68 |
| Pfam | ZU5 |
| SMART | DEATH |
| SMART | LRR_BAC |
| SMART | LRR_TYP |

**染色质调控潜力分析**: 18 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|
| CRADD | 0 |  | no |
| CASP2 | 0 |  | no |
| TP53 | 0 |  | no |
| BID | 0 |  | no |
| RIPK1 | 0 |  | no |
| FADD | 0 |  | no |
| ATM | 0 |  | no |
| IKBKG | 0 |  | no |
| TNFRSF10B | 0 |  | no |
| PRKDC | 0 |  | no |

**已知复合体成员** (GO-CC):

- C:endopeptidase complex (GO:1905369, IPI:ComplexPortal)


**PPI 互证分析**:
- （待补充：综合 STRING、IntAct 和 GO 数据库的互作信息，分析 PPI 网络的一致性）
**评价**: STRING 15 个互作伙伴，调控相关性低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 1 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 18 个 | 多库一致 |
| PPI 网络 | STRING | 15 个 | 单一来源 |
| 核定位 | HPA/UniProt/GO | Nucleus | Partially consistent |

**互证加分明细**:
PDB + AlphaFold 结构互证 (+0.5)
多库结构域一致 (+0.5)
**总计**: +1.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 44 篇，高度新颖
2. 核定位: needs confirmation

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 1 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PIDD1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177595-PIDD1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PIDD1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9HB75
- STRING: https://string-db.org/network/9606.ENSG00000177595
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HB75


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PIDD1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/PIDD1/PIDD1-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000177595-PIDD1/subcellular

![](https://images.proteinatlas.org/55473/1036_D2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/55473/1036_D2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/55473/874_G8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/55473/874_G8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/55473/881_G8_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/55473/881_G8_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
