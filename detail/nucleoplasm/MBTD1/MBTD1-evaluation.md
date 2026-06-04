---
type: protein-evaluation
gene: "MBTD1"
date: 2026-01-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MBTD1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | MBTD1 |
| 别名 | FLJ20055 |
| 基因全称 | mbt domain containing 1 |
| 蛋白名称 | MBT domain-containing protein 1 |
| 蛋白大小 | 628 aa |
| UniProt ID | Q05BQ5 |
| 评估日期 | 2026-01-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| Nucleus 核定位特异性 | 8/10 | x4 | 32 | HPA: Nuclear bodies, Nucleoplasm |
| Size 蛋白大小 | 10/10 | x1 | 10 | 628 aa |
| Novelty 研究新颖性 | 2/10 | x5 | 30 | PubMed: 95 篇 |
| 3D Structure 三维结构 | 7/10 | x3 | 21 | AlphaFold pLDDT=79.3 |
| Domain 调控结构域 | 7/10 | x2 | 14 | 含 MBT 结构域，可识别甲基化组蛋白 |
| PPI Network PPI网络 | 2/10 | x3 | 6 | STRING+IntAct+GO-CC |
| Cross-validation 互证加分 | — | max +3 | +1.5 | — |
|  | **原始总分** |  | **94.5/183** | **93.0/183** |  |  |  |
|  | **归一化总分** |  | **51.6/100** | **50.8/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | U-251MG, A-431 | HPA validated |
| UniProt | Nucleus/centromere/kinetochore | — |
| GO-CC | GO:0005634 Nucleus (IEA) | — |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MBTD1/IF_images/A_431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MBTD1/IF_images/U_251MG_1.jpg|U-251MG]]
#### 3.2 蛋白大小评估

628 aa，适合生化实验和结构解析

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 95 篇 |
| 最早发表年份 | 2026 |

**主要研究方向**:
- 功能研究尚不充分，属新颖蛋白

**关键文献**:
1. Takubo K et al. (2023). "MBTD1 preserves adult hematopoietic stem cell pool size and function.". *Proc Natl Acad Sci U S A*. PMID: 37523546
2. Qian J et al. (2025). "BET family BRD3 initiates DSB-induced chromatin remodeling with TIP60 to promote R-loop-mediated HR.". *Cell Rep*. PMID: 41134669
3. Chadchan SB et al. (2020). "A Role for Malignant Brain Tumor Domain-Containing Protein 1 in Human Endometrial Stromal Cell Decidualization.". *Front Cell Dev Biol*. PMID: 32850854
4. Wu W et al. (2019). "Overexpression of malignant brain tumor domain containing protein 1 predicts a poor prognosis of prostate cancer.". *Oncol Lett*. PMID: 30944653
5. Zhang H et al. (2020). "Structural Basis for EPC1-Mediated Recruitment of MBTD1 into the NuA4/TIP60 Acetyltransferase Complex.". *Cell Rep*. PMID: 32209463


**评价**: PubMed 95 篇，属有一定研究基础蛋白，研究空间充足。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 79.3 |
| pLDDT > 90 占比 | 61.5% |
| pLDDT 70-90 占比 | 10.0% |
| pLDDT 50-70 占比 | 6.2% |
| pLDDT < 50 占比 | 22.3% |
| 可用 PDB 条目 | 3 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MBTD1/MBTD1-PAE.png]]

**评价**: AlphaFold 预测中等质量，部分区域有序 (AlphaFold v6, pLDDT=79.3, >90=62%, 70-90=10%, 50-70=6%, <50=22%. PDB entries: 3FEO, 4C5I, 6NFX)

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | — |

**染色质调控潜力分析**: 含 MBT 结构域，可识别甲基化组蛋白

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-5666902|uniprotkb:Q9NXU1|uniprotkb:Q6ZVU7|ensembl:ENSP00000403946.1|ensembl:ENSP00000468304.1 | MI:0399(two hybrid fragment pooling | PMID:pubmed:23414517|imex:IM-16425 | — | — |
| intact:EBI-486838|uniprotkb:O15387|uniprotkb:A4D2A3|ensembl:ENSP00000304102.3 | MI:0676(tandem affinity purificatio | PMID:pubmed:21145461|imex:IM-18651|doi:10.1016/j.cell.2010.11.017 | — | — |
| intact:EBI-297903|intact:EBI-1103289|intact:EBI-1103265|intact:EBI-1055056|uniprotkb:Q15148|uniprotkb:Q16640|uniprotkb:Q6S376|intact:EBI-28976159|uniprotkb:Q6S380|intact:EBI-1103313|uniprotkb:Q6S377|uniprotkb:Q6S378|uniprotkb:Q6S379|intact:EBI-1103301|intact:EBI-1103253|uniprotkb:Q6S381|uniprotkb:Q6S382|uniprotkb:Q6S383|intact:EBI-2825763|ensembl:ENSP00000323856.4 | MI:0030(cross-linking study) | PMID:pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 | — | — |
| intact:EBI-20795332|ensembl:ENSP00000344955.4 | MI:0007(anti tag coimmunoprecipitat | PMID:pubmed:27153538|imex:IM-27061 | — | — |
| intact:EBI-769270|uniprotkb:Q8NAQ4|uniprotkb:Q8NE21|uniprotkb:Q96LF4|uniprotkb:Q96RR6|uniprotkb:Q9H7T7|uniprotkb:Q5VW54|uniprotkb:Q5VW56|uniprotkb:Q5VW58|uniprotkb:B4DSC3|uniprotkb:D3DRX7|ensembl:ENSP00000263062.8 | MI:0007(anti tag coimmunoprecipitat | PMID:pubmed:27153538|imex:IM-27061 | — | — |
|

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| MEAF6 | 0.0 | — | — |
| KAT5 | 0.0 | — | — |
| MORF4L1 | 0.0 | — | — |
| BRD8 | 0.0 | — | — |
| YEATS4 | 0.0 | — | — |
| RUVBL2 | 0.0 | — | — |
| DMAP1 | 0.0 | — | — |
| RUVBL1 | 0.0 | — | — |
|

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 复合体注释


**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 15
- 仅 IntAct 实验: 5
- 调控相关比例: 0/15 (0%)

**评价**: PPI 得分 2/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=79.3, PDB=3 | — |
| 结构域 | UniProt/InterPro | 无注释域 | — |
| PPI | STRING + IntAct + GO-CC | 15/5/0 条目 | — |
| 定位 | HPA/UniProt/GO | Nuclear bodies, Nucleoplasm / Nucleus / GO:0005634 | 一致 |

**互证加分明细**:
- PDB+AlphaFold 双源确认 (+0.5)
- IntAct+STRING 双源确认 (+0.5)
- PDB 多条目 (>=3) (+0.5)
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ★★ (3/5)

**核心优势**:
1. 有一定研究基础 (PubMed 95 篇)，几乎未被研究
2. HPA 确认核定位，高置信度

**风险/不确定性**:
1. AlphaFold 结构预测置信度较高
2. PPI 数据丰富，功能网络尚不清晰

**下一步建议**:
- [ ] 通过 IF 实验验证内源核定位
- [ ] 构建表达载体进行功能研究
- [ ] Co-IP/MS 鉴定互作蛋白

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=MBTD1
- Protein Atlas: https://www.proteinatlas.org/MBTD1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MBTD1
- UniProt: https://www.uniprot.org/uniprotkb/Q05BQ5
- SMART: http://smart.embl.de/
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q05BQ5


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MBTD1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MBTD1/MBTD1-PAE.png]]




