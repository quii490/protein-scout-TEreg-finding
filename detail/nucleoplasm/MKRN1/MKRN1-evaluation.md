---
type: protein-evaluation
gene: "MKRN1"
date: 2026-01-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MKRN1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | MKRN1 |
| 别名 | RNF61 |
| 基因全称 | makorin ring finger protein 1 |
| 蛋白名称 | E3 ubiquitin-protein ligase makorin-1 |
| 蛋白大小 | 482 aa |
| UniProt ID | Q9UHC7 |
| 评估日期 | 2026-01-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| Nucleus 核定位特异性 | 8/10 | x4 | 32 | HPA: Nuclear membrane, Nucleoplasm |
| Size 蛋白大小 | 10/10 | x1 | 10 | 482 aa |
| Novelty 研究新颖性 | 6/10 | x5 | 30 | PubMed: 59 篇 |
| 3D Structure 三维结构 | 7/10 | x3 | 21 | AlphaFold pLDDT=66.2 |
| Domain 调控结构域 | 7/10 | x2 | 14 | 含 RING finger 结构域，具有 E3 泛素连接酶活性 |
| PPI Network PPI网络 | 2/10 | x3 | 6 | STRING+IntAct+GO-CC |
| Cross-validation 互证加分 | — | max +3 | +0.5 | — |
| **原始总分** |  |  | **113.5/183** |  |
| **归一化总分** |  |  | **62.0/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | U-251MG, A-431 | HPA validated |
| UniProt | Nucleus | — |
| GO-CC | GO:0005634 Nucleus (IBA|IEA) | — |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MKRN1/IF_images/A_431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MKRN1/IF_images/U_251MG_1.jpg|U-251MG]]
#### 3.2 蛋白大小评估

482 aa，适合生化实验和结构解析

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 59 篇 |
| 最早发表年份 | 2026 |

**主要研究方向**:
- 功能研究尚不充分，属新颖蛋白

**关键文献**:
1. Deng L et al. (2024). "SF3A2 promotes progression and cisplatin resistance in triple-negative breast cancer via alternative splicing of MKRN1.". *Sci Adv*. PMID: 38569025
2. Roper N et al. (2020). "Clonal Evolution and Heterogeneity of Osimertinib Acquired Resistance Mechanisms in EGFR Mutant Lung Cancer.". *Cell Rep Med*. PMID: 32483558
3. Wang Y et al. (2025). "MKRN1 degrades AGC1 to trigger chemotherapy resistance of colorectal Cancer.". *Mol Med*. PMID: 40722058
4. Kim S et al. (2025). "Ebastine-mediated destabilization of E3 ligase MKRN1 protects against metabolic dysfunction-associated steatohepatitis.". *Cell Mol Life Sci*. PMID: 39888429
5. Jeong EB et al. (2019). "Makorin 1 is required for Drosophila oogenesis by regulating insulin/Tor signaling.". *PLoS One*. PMID: 31009498


**评价**: PubMed 59 篇，属有一定研究基础蛋白，研究空间充足。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 66.2 |
| pLDDT > 90 占比 | 19.3% |
| pLDDT 70-90 占比 | 28.6% |
| pLDDT 50-70 占比 | 19.9% |
| pLDDT < 50 占比 | 32.2% |
| 可用 PDB 条目 | 0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MKRN1/MKRN1-PAE.png]]

**评价**: AlphaFold 预测中等质量，部分区域有序 (AlphaFold v6, pLDDT=66.2, >90=19%, 70-90=29%, 50-70=20%, <50=32%)

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | — |

**染色质调控潜力分析**: 含 RING finger 结构域，具有 E3 泛素连接酶活性

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-146725 | MI:0018(two hybrid) | PMID:pubmed:14605208|imex:IM-16524|mint:MINT-5216804 | — | — |
| intact:EBI-123122|uniprotkb:Q4V428 | MI:0018(two hybrid) | PMID:pubmed:14605208|imex:IM-16524|mint:MINT-5216804 | — | — |
| intact:EBI-170802|uniprotkb:Q95TM0 | MI:1112(two hybrid prey pooling app | PMID:pubmed:unassigned1513|imex:IM-25777 | — | — |
| intact:EBI-196394|uniprotkb:Q9VFG6 | MI:0397(two hybrid array) | PMID:pubmed:37061542|imex:IM-28761 | — | — |
| intact:EBI-2810036|uniprotkb:Q6I0D7|uniprotkb:Q6KUA7|uniprotkb:E9QSG5|uniprotkb:E9QSG6|uniprotkb:Q81S56|uniprotkb:A0A0F7RJG7 | MI:0398(two hybrid pooling approach | PMID:imex:IM-13779|pubmed:20711500 | — | — |
|

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| TERT | 0.0 | — | — |
| PABPC1 | 0.0 | — | — |
| PABPC4 | 0.0 | — | — |
| HAGH | 0.0 | — | — |
| RNF130 | 0.0 | — | — |
| FAM131B | 0.0 | — | — |
| TP53 | 0.0 | — | — |
| IGF2BP3 | 0.0 | — | — |
|

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 复合体注释


**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 15
- 仅 IntAct 实验: 14
- 调控相关比例: 1/15 (7%)

**评价**: PPI 得分 2/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=66.2, PDB=0 | — |
| 结构域 | UniProt/InterPro | 无注释域 | — |
| PPI | STRING + IntAct + GO-CC | 15/14/0 条目 | — |
| 定位 | HPA/UniProt/GO | Nuclear membrane, Nucleoplasm / Nucleus / GO:0005634 | 一致 |

**互证加分明细**:
- IntAct+STRING 双源确认 (+0.5)
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ★★ (3/5)

**核心优势**:
1. 有一定研究基础 (PubMed 59 篇)，几乎未被研究
2. HPA 确认核定位，高置信度

**风险/不确定性**:
1. AlphaFold 预测质量中等 (pLDDT=66.2)，部分区域无序
2. PPI 数据丰富，功能网络尚不清晰

**下一步建议**:
- [ ] 通过 IF 实验验证内源核定位
- [ ] 构建表达载体进行功能研究
- [ ] Co-IP/MS 鉴定互作蛋白

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=MKRN1
- Protein Atlas: https://www.proteinatlas.org/MKRN1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MKRN1
- UniProt: https://www.uniprot.org/uniprotkb/Q9UHC7
- SMART: http://smart.embl.de/
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UHC7


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MKRN1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MKRN1/MKRN1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UHC7 |
| SMART | SM00184;SM00356; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR045072;IPR031644;IPR041367;IPR018957;IPR000571;IPR036855;IPR001841;IPR013083;IPR017907; |
| Pfam | PF15815;PF00097;PF00642;PF14608;PF18044; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000133606-MKRN1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CDKN1A | Intact, Biogrid | true |
| PABPC4 | Biogrid, Opencell | true |
| TP53 | Intact, Biogrid | true |
| APC | Biogrid | false |
| BYSL | Intact | false |
| CDKN2A | Biogrid | false |
| DAXX | Intact | false |
| ELAVL1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
