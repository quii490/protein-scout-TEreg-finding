---
type: protein-evaluation
gene: "PHF20L1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PHF20L1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PHF20L1 / CGI-72|FLJ13649|MGC64923|FLJ21615|TDRD20B |
| 蛋白全称 | PHD finger protein 20-like protein 1 |
| 蛋白大小 | 1017 aa |
| UniProt ID | A8MW92 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 8/10 | ×1 | **8** | 1017 aa，尚可接受 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 25 篇，高度新颖 |
| 三维结构 | 10/10 | ×3 | **30** | 9 个 PDB 结构 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: kdm4-like_tudor, phd20l1_u1, phd_5, tudor, tudor_2 |
| PPI 网络 | 4/10 | ×3 | **12** | STRING 15 个互作伙伴，调控相关性低 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **143/183** |  |
| **归一化总分** |  |  | **78.1/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | N/A | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PHF20L1/IF_images/A-431_HPA028417_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PHF20L1/IF_images/U-251MG_HPA028417_2.jpg|U-251MG]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 1017 aa，尚可接受

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 25 |

**评价**: PubMed 25 篇，高度新颖

**关键文献**:
1. Wang Y et al. (2025). "PHF20L1: An Epigenetic Regulator in Cancer and Beyond". *Biomolecules*. PMID: 40723918
2. Hou Y et al. (2020). "PHF20L1 as a H3K27me2 reader coordinates with transcriptional repressors to promote breast tumorigenesis". *Sci Adv*. PMID: 32494608
3. Wang Q et al. (2018). "PHF20L1 antagonizes SOX2 proteolysis triggered by the MLL1/WDR5 complexes". *Lab Invest*. PMID: 30089852
4. Syreeni A et al. (2021). "Genome-wide search for genes affecting the age at diagnosis of type 1 diabetes". *J Intern Med*. PMID: 33179336
5. Zhang C et al. (2019). "Proteolysis of methylated SOX2 protein is regulated by L3MBTL3 and CRL4(DCAF5) ubiquitin ligase". *J Biol Chem*. PMID: 30442713
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 1017 aa |
| PDB 条数 | 9 |
| 已注释结构域 | 14 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PHF20L1/PHF20L1-PAE.png]]

**评价**: 9 个 PDB 结构

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Agenet_dom_plant |
| InterPro | KDM4-like_Tudor |
| InterPro | PHF20-like |
| InterPro | Tudor |
| InterPro | Tudor_PHF20L1 |
| InterPro | Zinc_finger_PHD-type_CS |
| InterPro | Znf_FYVE_PHD |
| InterPro | Znf_RING/FYVE/PHD |
| Pfam | PHD20L1_u1 |
| Pfam | PHD_5 |
| Pfam | Tudor_2 |
| SMART | Agenet |
| SMART | TUDOR |
| PROSITE | ZF_PHD_1 |

**染色质调控潜力分析**: 染色质/DNA 结构域: kdm4-like_tudor, phd20l1_u1, phd_5, tudor, tudor_2

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|
| KANSL1 | 0 |  | no |
| KAT8 | 0 |  | no |
| KANSL3 | 0 |  | no |
| KANSL2 | 0 |  | no |
| MCRS1 | 0 |  | no |
| CHD3 | 0 |  | no |
| GATAD2B | 0 |  | no |
| BCL11A | 0 |  | no |
| GATAD2A | 0 |  | no |
| MBD2 | 0 |  | no |

**已知复合体成员** (GO-CC):

- C:NSL complex (GO:0044545, IBA:GO_Central)

**评价**: STRING 15 个互作伙伴，调控相关性低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 9 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 14 个 | 多库一致 |
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
1. 新颖性: PubMed 25 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 9 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PHF20L1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000129292-PHF20L1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PHF20L1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/A8MW92
- STRING: https://string-db.org/network/9606.ENSG00000129292
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A8MW92


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PHF20L1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PHF20L1/PHF20L1-PAE.png]]




