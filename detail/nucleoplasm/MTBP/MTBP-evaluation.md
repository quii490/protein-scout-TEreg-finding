---
type: protein-evaluation
gene: "MTBP"
date: 2026-01-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MTBP 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | MTBP |
| 别名 | — |
| 基因全称 | MDM2 binding protein |
| 蛋白名称 | Mdm2-binding protein |
| 蛋白大小 | 904 aa |
| UniProt ID | Q96DY7 |
| 评估日期 | 2026-01-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| Nucleus 核定位特异性 | 9/10 | x4 | 36 | HPA: Nucleoplasm (IDA supported) |
| Size 蛋白大小 | 8/10 | x1 | 8 | 904 aa |
| Novelty 研究新颖性 | 6/10 | x5 | 30 | PubMed: 56 篇 |
| 3D Structure 三维结构 | 6/10 | x3 | 18 | AlphaFold pLDDT=63.4 |
| Domain 调控结构域 | 7/10 | x2 | 14 | 与 MDM2/p53 通路相关 |
| PPI Network PPI网络 | 8/10 | x3 | 24 | STRING+IntAct+GO-CC |
| Cross-validation 互证加分 | — | max +3 | +1.0 | — |
| **原始总分** |  |  | **131/183** |  |
| **归一化总分** |  |  | **71.6/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | U-251MG, HEK293 | HPA validated |
| UniProt | Nucleus/PML body | — |
| GO-CC | GO:0005634 Nucleus (IBA|IDA|IEA) | — |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MTBP/IF_images/HEK293_1.jpg|HEK293]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MTBP/IF_images/U_251MG_1.jpg|U-251MG]]
#### 3.2 蛋白大小评估

904 aa，中等偏大

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 56 篇 |
| 最早发表年份 | 2026 |

**主要研究方向**:
- 功能研究尚不充分，属新颖蛋白

**关键文献**:
1. Maya-Mendoza A et al. (2018). "High speed of fork progression induces DNA replication stress and genomic instability.". *Nature*. PMID: 29950726
2. Li W et al. (2025). "Unveiling the enigmatic role of MTBP in pan-cancer: A bioinformatics perspective.". *Pathol Res Pract*. PMID: 40680629
3. Ranjan A et al. (2023). "Characterization of an Mtbp Hypomorphic Allele in a Diethylnitrosamine-Induced Liver Carcinogenesis Model.". *Cancers (Basel)*. PMID: 37760565
4. Thakur BL et al. (2025). "Selective interactions at pre-replication complexes categorize baseline and dormant origins.". *Nat Commun*. PMID: 40319014
5. Ferreira P et al. (2021). "MTBP phosphorylation controls DNA replication origin firing.". *Sci Rep*. PMID: 33608586


**评价**: PubMed 56 篇，属有一定研究基础蛋白，研究空间充足。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 63.4 |
| pLDDT > 90 占比 | 9.1% |
| pLDDT 70-90 占比 | 38.6% |
| pLDDT 50-70 占比 | 20.7% |
| pLDDT < 50 占比 | 31.6% |
| 可用 PDB 条目 | 0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MTBP/MTBP-PAE.png]]

**评价**: AlphaFold 预测较低质量，大部分区域无序 (AlphaFold v6, pLDDT=63.4, >90=9%, 70-90=39%, 50-70=21%, <50=32%)

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | — |

**染色质调控潜力分析**: 与 MDM2/p53 通路相关

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-2849136|uniprotkb:Q74TG8|uniprotkb:A0A0H2W5H4|uniprotkb:Q0WEC0|uniprotkb:Q7CIT1|uniprotkb:A0A384KWM5 | MI:0398(two hybrid pooling approach | PMID:imex:IM-13779|pubmed:20711500 | — | — |
| intact:EBI-394377|uniprotkb:Q5VUF3|uniprotkb:Q6ISB5|ensembl:ENSP00000370938.3 | MI:1314(proximity-dependent biotin  | PMID:pubmed:29568061|imex:IM-26301 | — | — |
| intact:EBI-457097|uniprotkb:Q2M3U6|uniprotkb:Q4W5P4|uniprotkb:Q6LER8|uniprotkb:A8K7B6|ensembl:ENSP00000274026.5 | MI:0007(anti tag coimmunoprecipitat | PMID:pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | — | — |
| intact:EBI-717614|uniprotkb:A0JP09|uniprotkb:Q9UED1|uniprotkb:B7Z2P2|uniprotkb:F5H814|ensembl:ENSP00000386854.2|ensembl:ENSP00000454157.1|ensembl:ENSP00000487174.1 | MI:0007(anti tag coimmunoprecipitat | PMID:imex:IM-24279|pubmed:26028330 | — | — |
| intact:EBI-752230|uniprotkb:O00266|uniprotkb:Q3KRB9|uniprotkb:Q5RHS8|uniprotkb:Q9BU83|ensembl:ENSP00000357697.4|ensembl:ENSP00000357698.2|ensembl:ENSP00000357699.2|ensembl:ENSP00000473260.2 | MI:0007(anti tag coimmunoprecipitat | PMID:pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 | — | — |
|

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| TICRR | 0.0 | — | — |
| MDM2 | 0.0 | — | — |
| TOPBP1 | 0.0 | — | — |
| RECQL4 | 0.0 | — | — |
| CDC45 | 0.0 | — | — |
| ZGRF1 | 0.0 | — | — |
| CCNC | 0.0 | — | — |
| CDK8 | 0.0 | — | — |
|

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 复合体注释


**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 15
- 仅 IntAct 实验: 8
- 调控相关比例: 5/15 (33%)

**评价**: PPI 得分 8/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=63.4, PDB=0 | — |
| 结构域 | UniProt/InterPro | 无注释域 | — |
| PPI | STRING + IntAct + GO-CC | 15/8/0 条目 | — |
| 定位 | HPA/UniProt/GO | Nucleoplasm / Nucleus / GO:0005634 | 一致 |

**互证加分明细**:
- GO-CC IDA 实验证据 (+0.5)
- IntAct+STRING 双源确认 (+0.5)
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ★★★ (4/5)

**核心优势**:
1. 有一定研究基础 (PubMed 56 篇)，几乎未被研究
2. HPA 确认核定位，高置信度

**风险/不确定性**:
1. AlphaFold 预测质量中等 (pLDDT=63.4)，部分区域无序
2. PPI 数据丰富，功能网络尚不清晰

**下一步建议**:
- [ ] 通过 IF 实验验证内源核定位
- [ ] 构建表达载体进行功能研究
- [ ] Co-IP/MS 鉴定互作蛋白

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=MTBP
- Protein Atlas: https://www.proteinatlas.org/MTBP
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MTBP
- UniProt: https://www.uniprot.org/uniprotkb/Q96DY7
- SMART: http://smart.embl.de/
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96DY7


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MTBP-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MTBP/MTBP-PAE.png]]




