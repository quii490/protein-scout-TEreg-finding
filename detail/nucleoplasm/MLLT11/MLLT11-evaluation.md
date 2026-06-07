---
type: protein-evaluation
gene: "MLLT11"
date: 2026-01-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MLLT11 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | MLLT11 |
| 别名 | AF1Q |
| 基因全称 | MLLT11 transcription factor 7 cofactor |
| 蛋白名称 | Protein AF1q |
| 蛋白大小 | 90 aa |
| UniProt ID | Q13015 |
| 评估日期 | 2026-01-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| Nucleus 核定位特异性 | 6/10 | x4 | 24 | HPA: Nucleoplasm (IDA supported) |
| Size 蛋白大小 | 5/10 | x1 | 5 | 90 aa |
| Novelty 研究新颖性 | 6/10 | x5 | 40 | PubMed: 47 篇 |
| 3D Structure 三维结构 | 6/10 | x3 | 18 | AlphaFold pLDDT=63.0 |
| Domain 调控结构域 | 7/10 | x2 | 14 | 无已注释染色质调控结构域 |
| PPI Network PPI网络 | 8/10 | x3 | 24 | STRING+IntAct+GO-CC |
| Cross-validation 互证加分 | — | max +3 | +1.0 | — |
|  | **原始总分** |  | **116/183** | **115.0/183** |  |  |  |
|  | **归一化总分** |  | **63.4/100** | **62.8/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | AF22, SH-SY5Y | HPA validated |
| UniProt |  | — |
| GO-CC | GO:0005634 Nucleus (IBA|IDA|IEA) | — |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MLLT11/IF_images/AF22_1.jpg|AF22]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MLLT11/IF_images/SH_SY5Y_1.jpg|SH-SY5Y]]
#### 3.2 蛋白大小评估

仅 90 aa，极小型蛋白

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 47 篇 |
| 最早发表年份 | 2026 |

**主要研究方向**:
- 功能研究尚不充分，属新颖蛋白

**关键文献**:
1. van Weelderen RE et al. (2024). "Optimized cytogenetic risk-group stratification of KMT2A-rearranged pediatric acute myeloid leukemia.". *Blood Adv*. PMID: 38621200
2. Wang Z et al. (2024). "Causal effect of thyroid cancer on secondary primary malignancies: findings from the UK Biobank and FinnGen cohorts.". *Front Immunol*. PMID: 39391305
3. Blommers M et al. (2024). "Cerebellar granule cell migration and folia development require Mllt11/Af1q/Tcf7c.". *Dev Neurobiol*. PMID: 38509451
4. Liu X et al. (2023). "MLLT11 siRNA Inhibits the Migration and Promotes the Apoptosis of MDA-MB-231 Breast Cancer Cells.". *Breast J*. PMID: 38075552
5. Yamada M et al. (2014). "MLLT11/AF1q is differentially expressed in maturing neurons during development.". *Gene Expr Patterns*. PMID: 24839873


**评价**: PubMed 47 篇，属非常新颖蛋白，研究空间充足。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 63.0 |
| pLDDT > 90 占比 | 0.0% |
| pLDDT 70-90 占比 | 38.9% |
| pLDDT 50-70 占比 | 33.3% |
| pLDDT < 50 占比 | 27.8% |
| 可用 PDB 条目 | 0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MLLT11/MLLT11-PAE.png]]

**评价**: AlphaFold 预测较低质量，大部分区域无序 (AlphaFold v6, pLDDT=63.0, >90=0%, 70-90=39%, 50-70=33%, <50=28%)

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | — |

**染色质调控潜力分析**: 无已注释染色质调控结构域

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-456129|uniprotkb:O75415|uniprotkb:Q569L3|uniprotkb:Q9UBI8|uniprotkb:B8ZZC3|uniprotkb:Q9UET7|uniprotkb:A8K536|ensembl:ENSP00000264414.4 | MI:0676(tandem affinity purificatio | PMID:pubmed:21145461|imex:IM-18651|doi:10.1016/j.cell.2010.11.017 | — | — |
| intact:EBI-6149376 | MI:0096(pull down) | PMID:pubmed:21911578|imex:IM-17703 | — | — |
| intact:EBI-6269719|ensembl:ENSP00000357917.3 | MI:0018(two hybrid) | PMID:pubmed:26079538|imex:IM-26244 | — | — |
| intact:EBI-6620336 | MI:0412(electrophoretic mobility su | PMID:pubmed:26079538|imex:IM-26244 | — | — |
| intact:EBI-711968|uniprotkb:Q8WVX0|uniprotkb:Q96EZ9|uniprotkb:A8K745|ensembl:ENSP00000221418.3|ensembl:ENSP00000489530.1 | MI:0007(anti tag coimmunoprecipitat | PMID:pubmed:29426014|imex:IM-26302|doi:10.1016/j.jmb.2018.01.021 | — | — |
|

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| KMT2A | 0.0 | — | — |
| AFF1 | 0.0 | — | — |
| TCF7 | 0.0 | — | — |
| MLLT6 | 0.0 | — | — |
| MLLT10 | 0.0 | — | — |
| ELL | 0.0 | — | — |
| MLLT1 | 0.0 | — | — |
| MLLT3 | 0.0 | — | — |
|

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 复合体注释


**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 15
- 仅 IntAct 实验: 14
- 调控相关比例: 5/15 (33%)

**评价**: PPI 得分 8/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=63.0, PDB=0 | — |
| 结构域 | UniProt/InterPro | 无注释域 | — |
| PPI | STRING + IntAct + GO-CC | 15/14/0 条目 | — |
| 定位 | HPA/UniProt/GO | Nucleoplasm / Nucleus / GO:0005634 | 一致 |

**互证加分明细**:
- GO-CC IDA 实验证据 (+0.5)
- IntAct+STRING 双源确认 (+0.5)
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ★★ (3/5)

**核心优势**:
1. 非常新颖 (PubMed 47 篇)，几乎未被研究
2. HPA 确认核定位，中等置信度

**风险/不确定性**:
1. AlphaFold 预测质量中等 (pLDDT=63.0)，部分区域无序
2. PPI 数据丰富，功能网络尚不清晰

**下一步建议**:
- [ ] 通过 IF 实验验证内源核定位
- [ ] 构建表达载体进行功能研究
- [ ] Co-IP/MS 鉴定互作蛋白

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=MLLT11
- Protein Atlas: https://www.proteinatlas.org/MLLT11
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MLLT11
- UniProt: https://www.uniprot.org/uniprotkb/Q13015
- SMART: http://smart.embl.de/
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13015


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MLLT11-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MLLT11/MLLT11-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q13015 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026778;IPR033461; |
| Pfam | PF15017; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000213190-MLLT11/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CUL3 | Biogrid | false |
| DNAJA4 | Biogrid | false |
| MAD2L2 | Biogrid | false |
| S100B | Intact | false |
| TCF7 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
