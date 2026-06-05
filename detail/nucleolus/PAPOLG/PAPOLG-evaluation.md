---
type: protein-evaluation
gene: "PAPOLG"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PAPOLG 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PAPOLG / FLJ12972 |
| 蛋白全称 | Poly(A) polymerase gamma |
| 蛋白大小 | 736 aa |
| UniProt ID | Q9BWT3 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/PAPOLG/IF_images/HEK293_1.jpg|HEK293]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/PAPOLG/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 736 aa，处于理想范围 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 13 篇，极度新颖 |
| 三维结构 | 8/10 | ×3 | **24** | 1 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: pap_ntpase, pola_pol_ntpase |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **143/183** |  |
| **归一化总分** |  |  | **78.1/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | GO:0005634 | IBA|IDA|IEA |

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 736 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 13 |

**关键文献**:
1. Wu et al. (2024). "RNA 3'end tailing safeguards cells against products of pervasive transcription termination.". *Nat Commun*. PMID: 39617768
2. Lee et al. (2021). "Genome-Wide Association Study of Susceptibility Loci for TCF3-PBX1 Acute Lymphoblastic Leukemia in Children.". *J Natl Cancer Inst*. PMID: 32882024
3. Hu et al. (2022). "Comprehensive analysis of GSEC/miR-101-3p/SNX16/PAPOLG axis in hepatocellular carcinoma.". *PLoS One*. PMID: 35482720
4. Shen et al. (2023). "Analysis of differentially expressed microRNAs in bovine mammary epithelial cells treated with lipoteichoic acid.". *J Anim Physiol Anim Nutr (Berl)*. PMID: 35997417
5. Armah et al. (2013). "A diet rich in high-glucoraphanin broccoli interacts with genotype to reduce discordance in plasma metabolite profiles by modulating mitochondrial function.". *Am J Clin Nutr*. PMID: 23964055
**评价**: PubMed 13 篇，极度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 736 aa |
| PDB 条数 | 1 |
| 已注释结构域 | 8 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/PAPOLG/PAPOLG-PAE.png]]

**评价**: 1 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | NT_sf |
| InterPro | NuclTrfase_I-like_C |
| InterPro | PolA_pol_cen_dom |
| InterPro | PolA_pol_NTPase |
| InterPro | PolA_pol_RNA-bd_dom |
| Pfam | PAP_central |
| Pfam | PAP_NTPase |
| Pfam | PAP_RNA-bind |

**染色质调控潜力分析**: 染色质/DNA 结构域: pap_ntpase, pola_pol_ntpase

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| PCBD1 | two hybrid array | 20211142 | — | — |
| LZTR1 | two hybrid array | 20211142 | — | — |
| NFYA | two hybrid array | 20211142 | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

--


**PPI 互证分析**:
- （待补充：综合 STRING、IntAct 和 GO 数据库的互作信息，分析 PPI 网络的一致性）
**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 1 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 8 个 | 多库一致 |
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
1. 新颖性: PubMed 13 篇，极度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 1 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PAPOLG
- Protein Atlas: https://www.proteinatlas.org/ENSG00000115421-PAPOLG
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PAPOLG%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9BWT3
- STRING: https://string-db.org/network/9606.ENSG00000115421
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BWT3


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PAPOLG-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/PAPOLG/PAPOLG-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000115421-PAPOLG/subcellular

![](https://images.proteinatlas.org/35349/716_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/35349/716_F6_4_red_green.jpg)
![](https://images.proteinatlas.org/35349/719_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/35349/719_F6_2_red_green.jpg)
![](https://images.proteinatlas.org/35349/764_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/35349/764_F6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
