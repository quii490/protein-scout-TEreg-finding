---
type: protein-evaluation
gene: "MKS1"
date: 2026-01-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MKS1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | MKS1 |
| 别名 | POC12, BBS13 |
| 基因全称 | MKS transition zone complex subunit 1 |
| 蛋白名称 | Tectonic-like complex member MKS1 |
| 蛋白大小 | 559 aa |
| UniProt ID | Q9NXB0 |
| 评估日期 | 2026-01-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| Nucleus 核定位特异性 | 8/10 | x4 | 32 | HPA: Nucleoplasm |
| Size 蛋白大小 | 10/10 | x1 | 10 | 559 aa |
| Novelty 研究新颖性 | 6/10 | x5 | 30 | PubMed: 58 篇 |
| 3D Structure 三维结构 | 7/10 | x3 | 21 | AlphaFold pLDDT=73.6 |
| Domain 调控结构域 | 7/10 | x2 | 14 | 与纤毛/中心体过渡区复合体相关 |
| PPI Network PPI网络 | 2/10 | x3 | 6 | STRING+IntAct+GO-CC |
| Cross-validation 互证加分 | — | max +3 | +0.5 | — |
| **原始总分** |  |  | **113.5/183** |  |
| **归一化总分** |  |  | **62.0/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | RPTEC/TERT1, ASC52telo | HPA validated |
| UniProt | Nucleus/Cytoplasm | — |
| GO-CC | GO:0005634 Nucleus (IBA|IEA|ISS) | — |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MKS1/IF_images/ASC52telo_1.jpg|ASC52telo]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MKS1/IF_images/RPTEC_TERT1_1.jpg|RPTEC/TERT1]]
#### 3.2 蛋白大小评估

559 aa，适合生化实验和结构解析

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 58 篇 |
| 最早发表年份 | 2025 |

**主要研究方向**:
- 功能研究尚不充分，属新颖蛋白

**关键文献**:
1. Adam MP et al. (1993). "Joubert Syndrome.". **. PMID: 20301500
2. Adam MP et al. (1993). "Bardet-Biedl Syndrome Overview.". **. PMID: 20301537
3. Qin Y et al. (2023). "Prenatal whole-exome sequencing for fetal structural anomalies: a retrospective analysis of 145 Chinese cases.". *BMC Med Genomics*. PMID: 37880672
4. Wang J et al. (2022). "Variable phenotypes and penetrance between and within different zebrafish ciliary transition zone mutants.". *Dis Model Mech*. PMID: 36533556
5. Szymanska K et al. (2022). "Regulation of canonical Wnt signalling by the ciliopathy protein MKS1 and the E2 ubiquitin-conjugating enzyme UBE2E1.". *Elife*. PMID: 35170427


**评价**: PubMed 58 篇，属有一定研究基础蛋白，研究空间充足。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 73.6 |
| pLDDT > 90 占比 | 13.2% |
| pLDDT 70-90 占比 | 54.9% |
| pLDDT 50-70 占比 | 19.0% |
| pLDDT < 50 占比 | 12.9% |
| 可用 PDB 条目 | 0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MKS1/MKS1-PAE.png]]

**评价**: AlphaFold 预测中等质量，部分区域有序 (AlphaFold v6, pLDDT=73.6, >90=13%, 70-90=55%, 50-70=19%, <50=13%)

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | — |

**染色质调控潜力分析**: 与纤毛/中心体过渡区复合体相关

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-7665|uniprotkb:Q03959|uniprotkb:D6W445 | MI:0363(inferred by author) | PMID:pubmed:16429126 | — | — |
| intact:EBI-19430|uniprotkb:Q01801|uniprotkb:Q05168|uniprotkb:D6VQC3|uniprotkb:Q6J5J4 | MI:0676(tandem affinity purificatio | PMID:pubmed:16429126 | — | — |
| intact:EBI-10978|uniprotkb:Q02533|uniprotkb:D6W1A3 | MI:0676(tandem affinity purificatio | PMID:pubmed:16429126 | — | — |
| intact:EBI-713081|uniprotkb:E7EMJ4|uniprotkb:Q4V9L5|ensembl:ENSP00000481495.1|ensembl:ENSP00000482106.1 | MI:0398(two hybrid pooling approach | PMID:pubmed:16169070|imex:IM-16517|mint:MINT-5217955 | — | — |
| intact:EBI-4281008|uniprotkb:Q6PDZ5|uniprotkb:Q8C0B3|uniprotkb:Q9CXF5|ensembl:ENSMUSP00000159383.2 | MI:0007(anti tag coimmunoprecipitat | PMID:pubmed:21565611|imex:IM-16529 | — | — |
|

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| CC2D2A | 0.0 | — | — |
| TCTN1 | 0.0 | — | — |
| TMEM67 | 0.0 | — | — |
| CEP290 | 0.0 | — | — |
| B9D1 | 0.0 | — | — |
| TCTN2 | 0.0 | — | — |
| TMEM216 | 0.0 | — | — |
| TMEM231 | 0.0 | — | — |
|

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 复合体注释


**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 15
- 仅 IntAct 实验: 8
- 调控相关比例: 1/15 (7%)

**评价**: PPI 得分 2/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=73.6, PDB=0 | — |
| 结构域 | UniProt/InterPro | 无注释域 | — |
| PPI | STRING + IntAct + GO-CC | 15/8/0 条目 | — |
| 定位 | HPA/UniProt/GO | Nucleoplasm / Nucleus / GO:0005634 | 一致 |

**互证加分明细**:
- IntAct+STRING 双源确认 (+0.5)
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ★★ (3/5)

**核心优势**:
1. 有一定研究基础 (PubMed 58 篇)，几乎未被研究
2. HPA 确认核定位，高置信度

**风险/不确定性**:
1. AlphaFold 结构预测置信度较高
2. PPI 数据丰富，功能网络尚不清晰

**下一步建议**:
- [ ] 通过 IF 实验验证内源核定位
- [ ] 构建表达载体进行功能研究
- [ ] Co-IP/MS 鉴定互作蛋白

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=MKS1
- Protein Atlas: https://www.proteinatlas.org/MKS1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MKS1
- UniProt: https://www.uniprot.org/uniprotkb/Q9NXB0
- SMART: http://smart.embl.de/
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NXB0


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MKS1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MKS1/MKS1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NXB0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 311..439; /note="C2 B9-type"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00713" |
| InterPro | IPR010796; |
| Pfam | PF07162; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000011143-MKS1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| B9D1 | Intact, Biogrid | true |
| B9D2 | Intact, Biogrid, Bioplex | true |
| BAG2 | Biogrid, Bioplex | true |
| TCTN2 | Biogrid, Bioplex | true |
| TMEM231 | Intact, Biogrid, Bioplex | true |
| DNAJA2 | Biogrid | false |
| NPAS1 | Bioplex | false |
| R3HCC1L | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
