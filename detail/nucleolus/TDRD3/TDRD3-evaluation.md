---
type: protein-evaluation
gene: "TDRD3"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TDRD3 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | TDRD3 / FLJ21007 |
| 蛋白全称 | Tudor domain-containing protein 3 |
| 蛋白大小 | 651 aa |
| UniProt ID | Q9H7E2 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TDRD3/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TDRD3/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | **28** | UniProt 核定位，部分细胞质 |
| 蛋白大小 | 10/10 | ×1 | **10** | 651 aa，处于理想范围 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 39 篇，高度新颖 |
| 三维结构 | 10/10 | ×3 | **30** | 20 个 PDB 结构 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: tudor, tudor_tdrd3 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **135/183** |  |
| **归一化总分** |  |  | **73.8/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Cytoplasm, Nucleus | 实验证据/预测 |
| GO-CC | GO:0005634 | IEA |

**结论**: UniProt Nucleus + partial cyto

#### 3.2 蛋白大小评估

**评价**: 651 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 39 |

**评价**: PubMed 39 篇，高度新颖

**关键文献**:
1. Su S et al. (2023). "A dual-activity topoisomerase complex promotes both transcriptional activation and repression in response to starvation". *Nucleic Acids Res*. PMID: 36794732
2. Morettin A et al. (2017). "Tudor Domain Containing Protein 3 Promotes Tumorigenesis and Invasive Capacity of Breast Cancer Cells". *Sci Rep*. PMID: 28698590
3. Yang Y et al. (2014). "Arginine methylation facilitates the recruitment of TOP3B to chromatin to prevent R loop accumulation". *Mol Cell*. PMID: 24507716
4. Saha S et al. (2023). "The TDRD3-USP9X complex and MIB1 regulate TOP3B homeostasis and prevent deleterious TOP3B cleavage complexes". *Nat Commun*. PMID: 37980342
5. Chen M et al. (2023). "Crystal structure of Tudor domain of TDRD3 in complex with a small molecule antagonist". *Biochim Biophys Acta Gene Regul Mech*. PMID: 37499935
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 651 aa |
| PDB 条数 | 20 |
| 已注释结构域 | 14 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TDRD3/TDRD3-PAE.png]]

**评价**: 20 个 PDB 结构

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | RMI1_N_C_sf |
| InterPro | RMI1_OB |
| InterPro | Tudor |
| InterPro | Tudor_TDRD3 |
| InterPro | UBA |
| InterPro | UBA-like_sf |
| InterPro | UBA_TDRD3 |
| Pfam | RMI1_N_C |
| Pfam | TUDOR |
| Pfam | UBA_7 |
| SMART | TUDOR |
| SMART | UBA |
| PROSITE | TUDOR |
| PROSITE | UBA |

**染色质调控潜力分析**: 染色质/DNA 结构域: tudor, tudor_tdrd3

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:DNA topoisomerase III-beta-TDRD3 complex (GO:0140225, IPI:ComplexPortal)
- F:chromatin binding (GO:0003682, IDA:UniProtKB)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 20 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 14 个 | 多库一致 |
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
1. 新颖性: PubMed 39 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 20 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=TDRD3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000083544-TDRD3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22TDRD3%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9H7E2
- STRING: https://string-db.org/network/9606.ENSG00000083544
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H7E2


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[TDRD3-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/TDRD3/TDRD3-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000083544-TDRD3/subcellular

![](https://images.proteinatlas.org/34925/942_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/34925/942_C1_2_red_green.jpg)
![](https://images.proteinatlas.org/34925/955_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/34925/955_C1_2_red_green.jpg)
![](https://images.proteinatlas.org/34925/972_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/34925/972_C1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H7E2 |
| SMART | SM00333;SM00165; |
| UniProt Domain [FT] | DOMAIN 193..233; /note="UBA"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00212"; DOMAIN 555..615; /note="Tudor"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00211" |
| InterPro | IPR042470;IPR013894;IPR002999;IPR047379;IPR015940;IPR009060;IPR041915; |
| Pfam | PF08585;PF00567;PF22562; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000083544-TDRD3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FMR1 | Intact, Biogrid | true |
| DCTN1 | Biogrid | false |
| DDX3X | Biogrid | false |
| DHX9 | Biogrid | false |
| EEF1A1 | Biogrid | false |
| EWSR1 | Biogrid | false |
| FBL | Biogrid | false |
| FUBP3 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
