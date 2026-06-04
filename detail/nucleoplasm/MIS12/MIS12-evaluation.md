---
type: protein-evaluation
gene: "MIS12"
date: 2026-01-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MIS12 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | MIS12 |
| 别名 | hMIS12, KNTC2AP, MTW1 |
| 基因全称 | MIS12 kinetochore complex component |
| 蛋白名称 | Protein MIS12 homolog |
| 蛋白大小 | 205 aa |
| UniProt ID | Q9H081 |
| 评估日期 | 2026-01-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| Nucleus 核定位特异性 | 8/10 | x4 | 32 | HPA: Nucleoplasm |
| Size 蛋白大小 | 10/10 | x1 | 10 | 205 aa |
| Novelty 研究新颖性 | 4/10 | x5 | 30 | PubMed: 74 篇 |
| 3D Structure 三维结构 | 10/10 | x3 | 30 | AlphaFold pLDDT=87.8 |
| Domain 调控结构域 | 7/10 | x2 | 14 | 无已注释染色质调控结构域 |
| PPI Network PPI网络 | 2/10 | x3 | 6 | STRING+IntAct+GO-CC |
| Cross-validation 互证加分 | — | max +3 | +1.5 | — |
|  | **原始总分** |  | **113.5/183** | **112.0/183** |  |  |  |
|  | **归一化总分** |  | **62.0/100** | **61.2/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

> **Protein Atlas IF**: 暂无HPA数据，核定位基于UniProt+GO

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA数据，核定位基于UniProt+GO | — |
| UniProt | Nucleus | — |
| GO-CC | GO:0005634 Nucleus (IBA|IEA) | — |

暂无 HPA IF 图片数据（Pending cell analysis），核定位基于 UniProt + GO 注释。


**结论**: 该蛋白在 HPA 中检测到Nucleoplasm信号，UniProt 注释为Nucleus。核定位得分 8/10。

#### 3.2 蛋白大小评估

205 aa，适合生化实验和结构解析

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 74 篇 |
| 最早发表年份 | 2026 |

**主要研究方向**:
- 功能研究尚不充分，属新颖蛋白

**关键文献**:
1. Girão H et al. (2024). "α-tubulin detyrosination fine-tunes kinetochore-microtubule attachments.". *Nat Commun*. PMID: 39521805
2. Asai K et al. (2024). "Artificial kinetochore beads establish a biorientation-like state in the spindle.". *Science*. PMID: 39298589
3. Zhang S et al. (2022). "FTO stabilizes MIS12 and counteracts senescence.". *Protein Cell*. PMID: 35384602
4. Perpelescu M et al. (2011). "The ABCs of CENPs.". *Chromosoma*. PMID: 21751032
5. Ladurner R et al. (2016). "MIS12/MIND Control at the Kinetochore.". *Cell*. PMID: 27814517


**评价**: PubMed 74 篇，属有一定研究基础蛋白，研究空间充足。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 87.8 |
| pLDDT > 90 占比 | 52.7% |
| pLDDT 70-90 占比 | 38.5% |
| pLDDT 50-70 占比 | 7.8% |
| pLDDT < 50 占比 | 1.0% |
| 可用 PDB 条目 | 4 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MIS12/MIS12-PAE.png]]

**评价**: AlphaFold 预测高质量，整体折叠良好 (AlphaFold v6, pLDDT=87.8, >90=53%, 70-90=38%, 50-70=8%, <50=1%. PDB entries: 5LSJ, 5LSK, 8PPR, 8Q5H)

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | — |

**染色质调控潜力分析**: 无已注释染色质调控结构域

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-1001205|uniprotkb:Q96N24|ensembl:ENSP00000370557.3|ensembl:ENSP00000461252.1|ensembl:ENSP00000484532.1 | MI:0676(tandem affinity purificatio | PMID:imex:IM-11719|pubmed:20360068 | — | — |
| intact:EBI-157363 | MI:1112(two hybrid prey pooling app | PMID:pubmed:unassigned1513|imex:IM-25777 | — | — |
| intact:EBI-15108077 | MI:1112(two hybrid prey pooling app | PMID:pubmed:unassigned1513|imex:IM-25777 | — | — |
| intact:EBI-162110 | MI:0397(two hybrid array) | PMID:pubmed:37061542|imex:IM-28761 | — | — |
| intact:EBI-124133|intact:EBI-498619|uniprotkb:Q7KU53|uniprotkb:Q7KU54|uniprotkb:Q8IQ39 | MI:0397(two hybrid array) | PMID:pubmed:37061542|imex:IM-28761 | — | — |
|

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| PMF1 | 0.0 | — | — |
| DSN1 | 0.0 | — | — |
| NSL1 | 0.0 | — | — |
| KNL1 | 0.0 | — | — |
| CENPC | 0.0 | — | — |
| SPC24 | 0.0 | — | — |
| NDC80 | 0.0 | — | — |
| ZWINT | 0.0 | — | — |
|

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 复合体注释


**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 15
- 仅 IntAct 实验: 7
- 调控相关比例: 1/15 (7%)

**评价**: PPI 得分 2/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=87.8, PDB=4 | — |
| 结构域 | UniProt/InterPro | 无注释域 | — |
| PPI | STRING + IntAct + GO-CC | 15/7/0 条目 | — |
| 定位 | HPA/UniProt/GO | Nucleoplasm / Nucleus / GO:0005634 | 一致 |

**互证加分明细**:
- PDB+AlphaFold 双源确认 (+0.5)
- IntAct+STRING 双源确认 (+0.5)
- PDB 多条目 (>=3) (+0.5)
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ★★ (3/5)

**核心优势**:
1. 有一定研究基础 (PubMed 74 篇)，几乎未被研究
2. HPA 确认核定位，高置信度

**风险/不确定性**:
1. AlphaFold 结构预测置信度较高
2. PPI 数据丰富，功能网络尚不清晰

**下一步建议**:
- [ ] 通过 IF 实验验证内源核定位
- [ ] 构建表达载体进行功能研究
- [ ] Co-IP/MS 鉴定互作蛋白

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=MIS12
- Protein Atlas: https://www.proteinatlas.org/MIS12
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MIS12
- UniProt: https://www.uniprot.org/uniprotkb/Q9H081
- SMART: http://smart.embl.de/
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H081


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MIS12-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MIS12/MIS12-PAE.png]]
