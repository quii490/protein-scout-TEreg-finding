---
type: protein-evaluation
gene: "SUPT16H"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SUPT16H 核蛋白评估报告

### 1. 基本信息

| 项目         | 内容                         |          |             |          |          |       |
| ---------- | -------------------------- | -------- | ----------- | -------- | -------- | ----- |
| 基因名 / 别名   | SUPT16H / FACT             | FACTP140 | SPT16/CDC68 | FLJ14010 | FLJ10857 | CDC68 |
| 蛋白全称       | FACT complex subunit SPT16 |          |             |          |          |       |
| 蛋白大小       | 1047 aa                    |          |             |          |          |       |
| UniProt ID | Q9Y5B9                     |          |             |          |          |       |
| 评估日期       | 2026-05-30                 |          |             |          |          |       |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/SUPT16H/IF_images/NIH-3T3_1.jpg|NIH 3T3]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/SUPT16H/IF_images/A-431_1.jpg|A-431]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 8/10 | ×1 | **8** | 1047 aa，尚可接受 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 33 篇，高度新颖 |
| 三维结构 | 10/10 | ×3 | **30** | 12 个 PDB 结构 |
| 调控结构域 | 7/10 | ×2 | **14** | 20 个已注释结构域 |
| PPI 网络 | 4/10 | ×3 | **12** | STRING 15 个互作伙伴，调控相关性低 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **137/183** |  |
| **归一化总分** |  |  | **74.9/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Nucleus, Chromosome | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 1047 aa，尚可接受

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 33 |

**评价**: PubMed 33 篇，高度新颖

**关键文献**:
1. Zhou D et al. (2022). "FACT subunit SUPT16H associates with BRD4 and contributes to silencing of interferon signaling". *Nucleic Acids Res*. PMID: 35904816
2. Hamanaka K et al. (2022). "Large-scale discovery of novel neurodevelopmental disorder-related genes through a unified analysis of single-nucleotide and copy number variants". *Genome Med*. PMID: 35468861
3. Eisfeldt J et al. (2024). "Resolving complex duplication variants in autism spectrum disorder using long-read genome sequencing". *Genome Res*. PMID: 39472019
4. Jeong E et al. (2022). "The FACT complex facilitates expression of lysosomal and antioxidant genes through binding to TFEB and TFE3". *Autophagy*. PMID: 35230915
5. Smol T et al. (2020). "Neurodevelopmental phenotype associated with CHD8-SUPT16H duplication". *Neurogenetics*. PMID: 31823155
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 1047 aa |
| PDB 条数 | 12 |
| 已注释结构域 | 20 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/SUPT16H/SUPT16H-PAE.png]]

**评价**: 12 个 PDB 结构

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Creatin/AminoP/Spt16_N |
| InterPro | Creatinase/aminopeptidase-like |
| InterPro | FACT-SPT16_Nlobe |
| InterPro | Fact-SPT16_PH |
| InterPro | FACT_SPT16_C |
| InterPro | FACT_SPT16_M |
| InterPro | Pept_M24 |
| InterPro | PH-like_dom_sf |
| InterPro | RTT106/SPT16-like_middle_dom |
| InterPro | Spt16 |
| InterPro | Spt16_M24 |
| Pfam | FACT-Spt16_Nlob |
| Pfam | Peptidase_M24 |
| Pfam | PH_SPT16 |
| Pfam | Rttp106-like_middle |

**染色质调控潜力分析**: 20 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|
| SSRP1 | 0 |  | no |
| SUPT5H | 0 |  | no |
| LEO1 | 0 |  | no |
| CTR9 | 0 |  | no |
| RTF1 | 0 |  | yes |
| SUPT6H | 0 |  | no |
| CDC73 | 0 |  | no |
| PAF1 | 0 |  | no |
| POLR2C | 0 |  | no |
| POLR2A | 0 |  | no |

**已知复合体成员** (GO-CC):

- C:FACT complex (GO:0035101, IPI:ComplexPortal)
- F:nucleosome binding (GO:0031491, IBA:GO_Central)
- P:nucleosome assembly (GO:0006334, NAS:ComplexPortal)
- P:nucleosome disassembly (GO:0006337, IDA:ComplexPortal)

**评价**: STRING 15 个互作伙伴，调控相关性低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 12 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 20 个 | 多库一致 |
| PPI 网络 | STRING | 15 个 | 单一来源 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
PDB + AlphaFold 结构互证 (+0.5)
多库结构域一致 (+0.5)
**总计**: +2.0

### 4. 总体评价

**推荐等级**: ****o (4/5)

**核心优势**:
1. 新颖性: PubMed 33 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 12 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SUPT16H
- Protein Atlas: https://www.proteinatlas.org/ENSG00000092201-SUPT16H
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SUPT16H%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9Y5B9
- STRING: https://string-db.org/network/9606.ENSG00000092201
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y5B9


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[SUPT16H-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/SUPT16H/SUPT16H-PAE.png]]




