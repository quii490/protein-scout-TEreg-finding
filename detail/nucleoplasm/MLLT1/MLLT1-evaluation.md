---
type: protein-evaluation
gene: "MLLT1"
date: 2026-01-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MLLT1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | MLLT1 |
| 别名 | ENL, YEATS1 |
| 基因全称 | MLLT1 super elongation complex subunit |
| 蛋白名称 | Protein ENL |
| 蛋白大小 | 559 aa |
| UniProt ID | Q03111 |
| 评估日期 | 2026-01-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| Nucleus 核定位特异性 | 8/10 | x4 | 32 | HPA: Nucleoplasm |
| Size 蛋白大小 | 10/10 | x1 | 10 | 559 aa |
| Novelty 研究新颖性 | 2/10 | x5 | 30 | PubMed: 90 篇 |
| 3D Structure 三维结构 | 6/10 | x3 | 18 | AlphaFold pLDDT=64.7 |
| Domain 调控结构域 | 7/10 | x2 | 14 | 含 YEATS 结构域，识别乙酰化/巴豆酰化组蛋白 |
| PPI Network PPI网络 | 8/10 | x3 | 24 | STRING+IntAct+GO-CC |
| Cross-validation 互证加分 | — | max +3 | +1.0 | — |
|  | **原始总分** |  | **109/183** | **108.0/183** |  |  |  |
|  | **归一化总分** |  | **59.6/100** | **59.0/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | U-251MG, A-431 | HPA validated |
| UniProt | Nucleus | — |
| GO-CC | GO:0005634 Nucleus (IBA|IEA|NAS) | — |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MLLT1/IF_images/A_431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MLLT1/IF_images/U_251MG_1.jpg|U-251MG]]
#### 3.2 蛋白大小评估

559 aa，适合生化实验和结构解析

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 90 篇 |
| 最早发表年份 | 2026 |

**主要研究方向**:
- 功能研究尚不充分，属新颖蛋白

**关键文献**:
1. van Weelderen RE et al. (2024). "Optimized cytogenetic risk-group stratification of KMT2A-rearranged pediatric acute myeloid leukemia.". *Blood Adv*. PMID: 38621200
2. Gadd S et al. (2017). "A Children's Oncology Group and TARGET initiative exploring the genetic landscape of Wilms tumor.". *Nat Genet*. PMID: 28825729
3. Perner F et al. (2026). "Targeting the Menin-KMT2A interaction in leukemia: Lessons learned and future directions.". *Int J Cancer*. PMID: 39887730
4. El Chaer F et al. (2020). "MLL-Rearranged Acute Lymphoblastic Leukemia.". *Curr Hematol Malig Rep*. PMID: 32350732
5. Isobe T et al. (2022). "Multi-omics analysis defines highly refractory RAS burdened immature subgroup of infant acute lymphoblastic leukemia.". *Nat Commun*. PMID: 36042201


**评价**: PubMed 90 篇，属有一定研究基础蛋白，研究空间充足。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 64.7 |
| pLDDT > 90 占比 | 33.3% |
| pLDDT 70-90 占比 | 4.8% |
| pLDDT 50-70 占比 | 15.6% |
| pLDDT < 50 占比 | 46.3% |
| 可用 PDB 条目 | 10 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MLLT1/MLLT1-PAE.png]]

**评价**: AlphaFold 预测较低质量，大部分区域无序 (AlphaFold v6, pLDDT=64.7, >90=33%, 70-90=5%, 50-70=16%, <50=46%. PDB entries: 5J9S, 6HPW, 6HPX, 6HPY, 6HPZ)

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | — |

**染色质调控潜力分析**: 含 YEATS 结构域，识别乙酰化/巴豆酰化组蛋白

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-6164389|uniprotkb:O09778 | MI:0096(pull down) | PMID:imex:IM-17346|pubmed:22190034|psi-mi:"MI:0007" | — | — |
| intact:EBI-1380405 | MI:0096(pull down) | PMID:pubmed:17721511|imex:IM-19952 | — | — |
| intact:EBI-1380407|chebi:"CHEBI:38943" | MI:0096(pull down) | PMID:pubmed:17721511|imex:IM-19952 | — | — |
| intact:EBI-927321|uniprotkb:O35699|uniprotkb:O35729|uniprotkb:Q4FJV5|uniprotkb:Q8C1X8|ensembl:ENSMUSP00000075476.5|ensembl:ENSMUSP00000140896.2 | MI:0096(pull down) | PMID:pubmed:17296600 | — | — |
| intact:EBI-2610180|intact:EBI-28974592|uniprotkb:B4DTU1|uniprotkb:E9PBM3|intact:EBI-11028221|ensembl:ENSP00000305689.6 | MI:0004(affinity chromatography tec | PMID:imex:IM-13603|pubmed:20153263 | — | — |
|

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| CCNT1 | 0.0 | — | — |
| ELL2 | 0.0 | — | — |
| AFF1 | 0.0 | — | — |
| CDK9 | 0.0 | — | — |
| MLLT3 | 0.0 | — | — |
| AFF4 | 0.0 | — | — |
| ELL | 0.0 | — | — |
| ELL3 | 0.0 | — | — |
|

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 复合体注释


**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 15
- 仅 IntAct 实验: 10
- 调控相关比例: 4/15 (27%)

**评价**: PPI 得分 8/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=64.7, PDB=10 | — |
| 结构域 | UniProt/InterPro | 无注释域 | — |
| PPI | STRING + IntAct + GO-CC | 15/10/0 条目 | — |
| 定位 | HPA/UniProt/GO | Nucleoplasm / Nucleus / GO:0005634 | 一致 |

**互证加分明细**:
- IntAct+STRING 双源确认 (+0.5)
- PDB 多条目 (>=3) (+0.5)
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ★★★ (4/5)

**核心优势**:
1. 有一定研究基础 (PubMed 90 篇)，几乎未被研究
2. HPA 确认核定位，高置信度

**风险/不确定性**:
1. AlphaFold 预测质量中等 (pLDDT=64.7)，部分区域无序
2. PPI 数据丰富，功能网络尚不清晰

**下一步建议**:
- [ ] 通过 IF 实验验证内源核定位
- [ ] 构建表达载体进行功能研究
- [ ] Co-IP/MS 鉴定互作蛋白

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=MLLT1
- Protein Atlas: https://www.proteinatlas.org/MLLT1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MLLT1
- UniProt: https://www.uniprot.org/uniprotkb/Q03111
- SMART: http://smart.embl.de/
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q03111


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MLLT1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MLLT1/MLLT1-PAE.png]]




