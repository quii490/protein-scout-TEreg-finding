---
type: protein-evaluation
gene: "MYSM1"
date: 2026-01-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MYSM1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | MYSM1 |
| 别名 | 2A-DUB |
| 基因全称 | Myb like, SWIRM and MPN domains 1 |
| 蛋白名称 | Deubiquitinase MYSM1 |
| 蛋白大小 | 828 aa |
| UniProt ID | Q5VVJ2 |
| 评估日期 | 2026-01-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| Nucleus 核定位特异性 | 9/10 | x4 | 36 | HPA: Nucleoli, Nucleoli fibrillar center (IDA supported) |
| Size 蛋白大小 | 8/10 | x1 | 8 | 828 aa |
| Novelty 研究新颖性 | 2/10 | x5 | 30 | PubMed: 85 篇 |
| 3D Structure 三维结构 | 6/10 | x3 | 18 | AlphaFold pLDDT=64.2 |
| Domain 调控结构域 | 7/10 | x2 | 14 | 含 Myb/SANT 和 SWIRM 结构域，染色质结合潜力 |
| PPI Network PPI网络 | 4/10 | x3 | 12 | STRING+IntAct+GO-CC |
| Cross-validation 互证加分 | — | max +3 | +1.0 | — |
|  | **原始总分** |  | **99/183** | **98.0/183** |  |  |  |
|  | **归一化总分** |  | **54.1/100** | **53.6/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | U-251MG, A-431 | HPA validated |
| UniProt | Nucleus/PML body/Cytoplasm | — |
| GO-CC | GO:0005634 Nucleus (IBA|IDA|IEA|TAS) | — |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MYSM1/IF_images/A_431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MYSM1/IF_images/U_251MG_1.jpg|U-251MG]]
#### 3.2 蛋白大小评估

828 aa，中等偏大

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 85 篇 |
| 最早发表年份 | 2026 |

**主要研究方向**:
- 功能研究尚不充分，属新颖蛋白

**关键文献**:
1. Zhao J et al. (2023). "Human hematopoietic stem cell vulnerability to ferroptosis.". *Cell*. PMID: 36803603
2. Shi X et al. (2024). "Deubiquitinase MYSM1 promotes doxorubicin-induced cardiotoxicity by mediating TRIM21-ferroptosis axis in cardiomyocytes.". *Cell Commun Signal*. PMID: 39695708
3. Zhong X et al. (2025). "MYSM1 Mediates Cardiac Parthanatos and Hypertrophy by Deubiquitinating PARP1.". *Hypertension*. PMID: 39907013
4. Qin Q et al. (2024). "Deubiquitinase MYSM1: An Important Tissue Development and Function Regulator.". *Int J Mol Sci*. PMID: 39684760
5. Xu Z et al. (2024). "Deubiquitinase Mysm1 regulates neural stem cell proliferation and differentiation by controlling Id4 expression.". *Cell Death Dis*. PMID: 38342917


**评价**: PubMed 85 篇，属有一定研究基础蛋白，研究空间充足。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 64.2 |
| pLDDT > 90 占比 | 23.8% |
| pLDDT 70-90 占比 | 27.9% |
| pLDDT 50-70 占比 | 7.5% |
| pLDDT < 50 占比 | 40.8% |
| 可用 PDB 条目 | 2 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MYSM1/MYSM1-PAE.png]]

**评价**: AlphaFold 预测较低质量，大部分区域无序 (AlphaFold v6, pLDDT=64.2, >90=24%, 70-90=28%, 50-70=8%, <50=41%. PDB entries: 2CU7, 2DCE)

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | — |

**染色质调控潜力分析**: 含 Myb/SANT 和 SWIRM 结构域，染色质结合潜力

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-394377|uniprotkb:Q5VUF3|uniprotkb:Q6ISB5|ensembl:ENSP00000370938.3 | MI:1314(proximity-dependent biotin  | PMID:pubmed:29568061|imex:IM-26301 | — | — |
| intact:EBI-79722|intact:EBI-1560041|uniprotkb:A0PJT7|uniprotkb:P02295|uniprotkb:P02296|uniprotkb:P16106|uniprotkb:Q6ISV8|uniprotkb:Q6NWP8|uniprotkb:Q6NWP9|uniprotkb:Q6NXU4|uniprotkb:Q71DJ3|uniprotkb:Q93081|uniprotkb:A5PLR1|ensembl:ENSP00000352252.3|ensembl:ENSP00000358160.2|ensembl:ENSP00000366999.2|ensembl:ENSP00000480826.2|ensembl:ENSP00000482271.1|ensembl:ENSP00000483283.2|ensembl:ENSP00000484095.2|ensembl:ENSP00000484638.1|ensembl:ENSP00000484658.2|ensembl:ENSP00000484841.2|ensembl:ENSP00000489282.1|ensembl:ENSP00000509120.1|ensembl:ENSP00000520711.1 | MI:1314(proximity-dependent biotin  | PMID:pubmed:29568061|imex:IM-26301 | — | — |
| intact:EBI-351935|uniprotkb:B4DI32|uniprotkb:E7EUI9|uniprotkb:P02546|uniprotkb:Q969I8|uniprotkb:Q96JA2|uniprotkb:D6RAQ3|uniprotkb:Q5I6Y4|uniprotkb:Q5I6Y6|uniprotkb:Q6UYC3|uniprotkb:Q5TCJ2|uniprotkb:Q5TCJ3|uniprotkb:D3DVB0|intact:EBI-28988787|ensembl:ENSP00000355292.6|ensembl:ENSP00000357283.4|ensembl:ENSP00000502256.1|ensembl:ENSP00000506771.1 | MI:1314(proximity-dependent biotin  | PMID:pubmed:29568061|imex:IM-26301 | — | — |
| intact:EBI-2514004|uniprotkb:B2RCC9|uniprotkb:Q5T2T0|uniprotkb:B5MDZ3|uniprotkb:Q8IY28|uniprotkb:D3DRW3|uniprotkb:B4DWL9|ensembl:ENSP00000337907.5|ensembl:ENSP00000364871.3|ensembl:ENSP00000364884.1|ensembl:ENSP00000507917.1 | MI:1356(validated two hybrid) | PMID:pubmed:32296183|imex:IM-25472 | — | — |
| intact:EBI-1051372|uniprotkb:B2R5H6|ensembl:ENSP00000361740.3|ensembl:ENSP00000361745.3|ensembl:ENSP00000496422.1 | MI:0007(anti tag coimmunoprecipitat | PMID:pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 | — | — |
|

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| KAT2B | 0.0 | — | — |
| H2AC20 | 0.0 | — | — |
| PBRM1 | 0.0 | — | — |
| SMARCB1 | 0.0 | — | — |
| H2AC18 | 0.0 | — | — |
| EP300 | 0.0 | — | — |
| PSMD6 | 0.0 | — | — |
| PSMD4 | 0.0 | — | — |
|

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 复合体注释


**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 15
- 仅 IntAct 实验: 7
- 调控相关比例: 2/15 (13%)

**评价**: PPI 得分 4/10。
##### PPI 数据源补充核查（自动审计）

**IntAct/BioGrid 实验互作核查**:
| Partner | 方法 | PMID |
|---------|------|------|
| — | proximity-dependent biotin identification | 29568061 |
| — | proximity-dependent biotin identification | 29568061 |
| — | proximity-dependent biotin identification | 29568061 |
| — | proximity-dependent biotin identification | 29568061 |
| — | proximity-dependent biotin identification | 29568061 |
| — | proximity-dependent biotin identification | 29568061 |
| — | validated two hybrid | 32296183 |
| — | two hybrid array | 32296183 |
| — | two hybrid prey pooling approach | 32296183 |
| — | anti tag coimmunoprecipitation | 33961781 |

**STRING 预测/整合互作核查**:
| Partner | Score |
|---------|-------|
| KAT2B | 0.985 |
| H2AC20 | 0.920 |
| PBRM1 | 0.914 |
| SMARCB1 | 0.851 |
| H2AC18 | 0.844 |
| EP300 | 0.839 |
| PSMD6 | 0.816 |
| PSMD4 | 0.809 |
| PSMC1 | 0.808 |
| PSMB2 | 0.801 |

**GO-CC 复合体/定位核查**:
- GO:0005737: cytoplasm (IEA:UniProtKB-SubCell)
- GO:0005730: nucleolus (IDA:HPA)
- GO:0005654: nucleoplasm (IDA:HPA)
- GO:0005634: nucleus (IDA:UniProtKB)
- GO:0032991: protein-containing complex (IPI:UniProtKB)

**补充结论**: PPI 评分仍以报告评分表为准；本节用于补齐 IntAct、STRING、GO-CC 三源审计证据。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=64.2, PDB=2 | — |
| 结构域 | UniProt/InterPro | 无注释域 | — |
| PPI | STRING + IntAct + GO-CC | 15/7/0 条目 | — |
| 定位 | HPA/UniProt/GO | Nucleoli, Nucleoli fibrillar center / Nucleus / GO:0005634 | 一致 |

**互证加分明细**:
- GO-CC IDA 实验证据 (+0.5)
- IntAct+STRING 双源确认 (+0.5)
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ★★ (3/5)

**核心优势**:
1. 有一定研究基础 (PubMed 85 篇)，几乎未被研究
2. HPA 确认核定位，高置信度

**风险/不确定性**:
1. AlphaFold 预测质量中等 (pLDDT=64.2)，部分区域无序
2. PPI 数据丰富，功能网络尚不清晰

**下一步建议**:
- [ ] 通过 IF 实验验证内源核定位
- [ ] 构建表达载体进行功能研究
- [ ] Co-IP/MS 鉴定互作蛋白

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=MYSM1
- Protein Atlas: https://www.proteinatlas.org/MYSM1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MYSM1
- UniProt: https://www.uniprot.org/uniprotkb/Q5VVJ2
- SMART: http://smart.embl.de/
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5VVJ2

![[MYSM1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MYSM1/MYSM1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5VVJ2 |
| SMART | SM00232;SM00717; |
| UniProt Domain [FT] | DOMAIN 116..167; /note="SANT"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00624"; DOMAIN 372..470; /note="SWIRM"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00247"; DOMAIN 577..709; /note="MPN"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01182" |
| InterPro | IPR009057;IPR000555;IPR050242;IPR037518;IPR017930;IPR001005;IPR017884;IPR007526;IPR036388; |
| Pfam | PF01398;PF00249;PF04433; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000162601-MYSM1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| H2AC20 | Biogrid | false |
| H2AX | Biogrid | false |
| HELLS | Biogrid | false |
| KAT2B | Biogrid | false |
| MPP7 | Intact | false |
| RFC5 | Biogrid | false |
| STING1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
