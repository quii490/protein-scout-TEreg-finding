---
type: protein-evaluation
gene: "MEPCE"
date: 2026-01-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MEPCE 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | MEPCE |
| 别名 | Bin3, FLJ20257 |
| 基因全称 | methylphosphate capping enzyme |
| 蛋白名称 | 7SK snRNA methylphosphate capping enzyme |
| 蛋白大小 | 689 aa |
| UniProt ID | Q7L2J0 |
| 评估日期 | 2026-01-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| Nucleus 核定位特异性 | 6/10 | x4 | 24 | HPA: Nuclear bodies (IDA supported) |
| Size 蛋白大小 | 10/10 | x1 | 10 | 689 aa |
| Novelty 研究新颖性 | 6/10 | x5 | 40 | PubMed: 42 篇 |
| 3D Structure 三维结构 | 6/10 | x3 | 18 | AlphaFold pLDDT=62.7 |
| Domain 调控结构域 | 7/10 | x2 | 14 | 含甲基转移酶结构域，参与 7SK snRNA 加工 |
| PPI Network PPI网络 | 2/10 | x3 | 6 | STRING+IntAct+GO-CC |
| Cross-validation 互证加分 | — | max +3 | +1.5 | — |
|  | **原始总分** |  | **103.5/183** | **102.0/183** |  |  |  |
|  | **归一化总分** |  | **56.6/100** | **55.7/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | U-251MG, A-431 | HPA validated |
| UniProt | Nucleus/Cytoplasm/Mitochondrion | — |
| GO-CC | GO:0005634 Nucleus (IDA|IEA) | — |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MEPCE/IF_images/A_431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MEPCE/IF_images/U_251MG_1.jpg|U-251MG]]
#### 3.2 蛋白大小评估

689 aa，适合生化实验和结构解析

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 42 篇 |
| 最早发表年份 | 2025 |

**主要研究方向**:
- 功能研究尚不充分，属新颖蛋白

**关键文献**:
1. Yang Y et al. (2022). "Structural basis of RNA conformational switching in the transcriptional regulator 7SK RNP.". *Mol Cell*. PMID: 35320752
2. Devanathan SK et al. (2025). "MePCE promotes homologous recombination through coordinating R-loop resolution at DNA double-stranded breaks.". *Cell Rep*. PMID: 40411785
3. Wang Z et al. (2024). "The phosphatase PP1 sustains global transcription by promoting RNA polymerase II pause release.". *Mol Cell*. PMID: 39603240
4. Leventhal MJ et al. (2025). "An integrative systems-biology approach defines mechanisms of Alzheimer's disease neurodegeneration.". *Nat Commun*. PMID: 40393985
5. Kao TL et al. (2024). "LARP3, LARP7, and MePCE are involved in the early stage of human telomerase RNA biogenesis.". *Nat Commun*. PMID: 39009594


**评价**: PubMed 42 篇，属非常新颖蛋白，研究空间充足。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 62.7 |
| pLDDT > 90 占比 | 29.5% |
| pLDDT 70-90 占比 | 9.6% |
| pLDDT 50-70 占比 | 11.6% |
| pLDDT < 50 占比 | 49.3% |
| 可用 PDB 条目 | 5 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MEPCE/MEPCE-PAE.png]]

**评价**: AlphaFold 预测较低质量，大部分区域无序 (AlphaFold v6, pLDDT=62.7, >90=30%, 70-90=10%, 50-70=12%, <50=49%. PDB entries: 5UNA, 6DCB, 6DCC, 7SLP, 7SLQ)

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | — |

**染色质调控潜力分析**: 含甲基转移酶结构域，参与 7SK snRNA 加工

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-6164389|uniprotkb:O09778 | MI:0007(anti tag coimmunoprecipitat | PMID:imex:IM-17346|pubmed:22190034|psi-mi:"MI:0007" | — | — |
| intact:EBI-2370740|ensembl:ENSP00000294008.3|uniprotkb:Q69YT8|uniprotkb:Q8TF15|uniprotkb:Q96JP1|intact:EBI-2560942 | MI:0007(anti tag coimmunoprecipitat | PMID:imex:IM-12200|pubmed:19596235 | — | — |
| intact:EBI-1043104|uniprotkb:Q9HCA6|uniprotkb:Q9UNP0|uniprotkb:Q9Y5B5|uniprotkb:Q9H8G9|uniprotkb:Q08AL5|ensembl:ENSP00000280377.5 | MI:0007(anti tag coimmunoprecipitat | PMID:imex:IM-12079|pubmed:19615732 | — | — |
| intact:EBI-718395|uniprotkb:O43445|uniprotkb:O43864|uniprotkb:Q96DG2|uniprotkb:Q96IK4|uniprotkb:Q5T1M8|ensembl:ENSP00000363315.4 | MI:0007(anti tag coimmunoprecipitat | PMID:imex:IM-12079|pubmed:19615732 | — | — |
| intact:EBI-308619|uniprotkb:Q2M2H0|uniprotkb:Q58F06|uniprotkb:Q8IUS1|uniprotkb:Q96J95|uniprotkb:A8K2E4|intact:EBI-11138149|uniprotkb:B7ZKM0|ensembl:ENSP00000449386.2 | MI:0007(anti tag coimmunoprecipitat | PMID:imex:IM-12079|pubmed:19615732 | — | — |
|

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| LARP7 | 0.0 | — | — |
| HEXIM1 | 0.0 | — | — |
| HEXIM2 | 0.0 | — | — |
| CDK9 | 0.0 | — | — |
| CCNT1 | 0.0 | — | — |
| SART3 | 0.0 | — | — |
| BIN3 | 0.0 | — | — |
| CCNT2 | 0.0 | — | — |
|

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 复合体注释


**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 15
- 仅 IntAct 实验: 17
- 调控相关比例: 1/15 (7%)

**评价**: PPI 得分 2/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=62.7, PDB=5 | — |
| 结构域 | UniProt/InterPro | 无注释域 | — |
| PPI | STRING + IntAct + GO-CC | 15/17/0 条目 | — |
| 定位 | HPA/UniProt/GO | Nuclear bodies / Nucleus / GO:0005634 | 一致 |

**互证加分明细**:
- GO-CC IDA 实验证据 (+0.5)
- IntAct+STRING 双源确认 (+0.5)
- PDB 多条目 (>=3) (+0.5)
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ★★ (3/5)

**核心优势**:
1. 非常新颖 (PubMed 42 篇)，几乎未被研究
2. HPA 确认核定位，中等置信度

**风险/不确定性**:
1. AlphaFold 预测质量中等 (pLDDT=62.7)，部分区域无序
2. PPI 数据丰富，功能网络尚不清晰

**下一步建议**:
- [ ] 通过 IF 实验验证内源核定位
- [ ] 构建表达载体进行功能研究
- [ ] Co-IP/MS 鉴定互作蛋白

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=MEPCE
- Protein Atlas: https://www.proteinatlas.org/MEPCE
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MEPCE
- UniProt: https://www.uniprot.org/uniprotkb/Q7L2J0
- SMART: http://smart.embl.de/
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7L2J0


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MEPCE-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MEPCE/MEPCE-PAE.png]]




