---
type: protein-evaluation
gene: "MAGEB16"
date: 2026-01-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MAGEB16 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | MAGEB16 |
| 别名 | MAGE-B16 |
| 基因全称 | MAGE family member B16 |
| 蛋白名称 | Melanoma-associated antigen B16 |
| 蛋白大小 | 324 aa |
| UniProt ID | A2A368 |
| 评估日期 | 2026-01-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| Nucleus 核定位特异性 | 6/10 | x4 | 24 | HPA: Nucleoli, Nucleoplasm |
| Size 蛋白大小 | 10/10 | x1 | 10 | 324 aa |
| Novelty 研究新颖性 | 10/10 | x5 | 50 | PubMed: 9 篇 |
| 3D Structure 三维结构 | 7/10 | x3 | 21 | AlphaFold pLDDT=74.2 |
| Domain 调控结构域 | 7/10 | x2 | 14 | MAGE 家族成员，癌症/睾丸抗原 |
| PPI Network PPI网络 | 2/10 | x3 | 6 | STRING+IntAct+GO-CC |
| Cross-validation 互证加分 | — | max +3 | +0.5 | — |
| **原始总分** |  |  | **125.5/183** |  |
| **归一化总分** |  |  | **68.6/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | K-562 | HPA validated |
| UniProt | Chromosome | — |
| GO-CC | GO:0005634 Nucleus () | — |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MAGEB16/IF_images/K_562_1.jpg|K-562]]
#### 3.2 蛋白大小评估

324 aa，适合生化实验和结构解析

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 9 篇 |
| 最早发表年份 | 2026 |

**主要研究方向**:
- 功能研究尚不充分，属新颖蛋白

**关键文献**:
1. Gaspar JA et al. (2017). "Depletion of Mageb16 induces differentiation of pluripotent stem cells predominantly into mesodermal derivatives.". *Sci Rep*. PMID: 29079788
2. Juhari WKW et al. (2021). "Whole-Genome Profiles of Malay Colorectal Cancer Patients with Intact MMR Proteins.". *Genes (Basel)*. PMID: 34573430
3. Liu Y et al. (2014). "Demethylation of CpG islands in the 5' upstream regions mediates the expression of the human testis-specific gene MAGEB16 and its mouse homolog Mageb16.". *BMB Rep*. PMID: 24219866
4. Zaragoza-Huesca D et al. (2022). "Identification of Thrombosis-Related Genes in Patients with Advanced Gastric Cancer: Data from AGAMENON-SEOM Registry.". *Biomedicines*. PMID: 35052827
5. Wu X et al. (2025). "Knockdown of Mageb16 disrupts cell proliferation and lineage specification during mouse preimplantation development.". *Theriogenology*. PMID: 40117938


**评价**: PubMed 9 篇，属极度新颖蛋白，研究空间充足。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 74.2 |
| pLDDT > 90 占比 | 42.0% |
| pLDDT 70-90 占比 | 19.8% |
| pLDDT 50-70 占比 | 12.7% |
| pLDDT < 50 占比 | 25.6% |
| 可用 PDB 条目 | 0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MAGEB16/MAGEB16-PAE.png]]

**评价**: AlphaFold 预测中等质量，部分区域有序 (AlphaFold v6, pLDDT=74.2, >90=42%, 70-90=20%, 50-70=13%, <50=26%)

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | — |

**染色质调控潜力分析**: MAGE 家族成员，癌症/睾丸抗原

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-743122|uniprotkb:Q14798|ensembl:ENSP00000276344.2|ensembl:ENSP00000353379.2|ensembl:ENSP00000359360.1|ensembl:ENSP00000359365.3|ensembl:ENSP00000377497.1|ensembl:ENSP00000377498.1|ensembl:ENSP00000394149.2|ensembl:ENSP00000402186.2|ensembl:ENSP00000506838.1|ensembl:ENSP00000507023.1 | MI:0007(anti tag coimmunoprecipitat | PMID:pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | — | — |
|

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| MAGEA4 | 0.0 | — | — |
| FAM209A | 0.0 | — | — |
| C12orf40 | 0.0 | — | — |
| C9orf131 | 0.0 | — | — |
| OR2L8 | 0.0 | — | — |
| C9orf43 | 0.0 | — | — |
| SLC22A24 | 0.0 | — | — |
| TMCO5A | 0.0 | — | — |
|

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 复合体注释


**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 15
- 仅 IntAct 实验: 1
- 调控相关比例: 0/15 (0%)

**评价**: PPI 得分 2/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=74.2, PDB=0 | — |
| 结构域 | UniProt/InterPro | 无注释域 | — |
| PPI | STRING + IntAct + GO-CC | 15/1/0 条目 | — |
| 定位 | HPA/UniProt/GO | Nucleoli, Nucleoplasm / Nucleus / GO:0005634 | 一致 |

**互证加分明细**:
- IntAct+STRING 双源确认 (+0.5)
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ★★ (3/5)

**核心优势**:
1. 极度新颖 (PubMed 9 篇)，几乎未被研究
2. HPA 确认核定位，中等置信度

**风险/不确定性**:
1. AlphaFold 结构预测置信度较高
2. PPI 数据丰富，功能网络尚不清晰

**下一步建议**:
- [ ] 通过 IF 实验验证内源核定位
- [ ] 构建表达载体进行功能研究
- [ ] Co-IP/MS 鉴定互作蛋白

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=MAGEB16
- Protein Atlas: https://www.proteinatlas.org/MAGEB16
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAGEB16
- UniProt: https://www.uniprot.org/uniprotkb/A2A368
- SMART: http://smart.embl.de/
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A2A368


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MAGEB16-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MAGEB16/MAGEB16-PAE.png]]




