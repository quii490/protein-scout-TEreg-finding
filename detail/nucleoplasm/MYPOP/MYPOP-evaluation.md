---
type: protein-evaluation
gene: "MYPOP"
date: 2026-01-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MYPOP 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | MYPOP |
| 别名 | P42pop |
| 基因全称 | Myb-related transcription factor, partner of profilin |
| 蛋白名称 | Myb-related transcription factor, partner of profilin |
| 蛋白大小 | 399 aa |
| UniProt ID | Q86VE0 |
| 评估日期 | 2026-01-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| Nucleus 核定位特异性 | 9/10 | x4 | 36 | HPA: Nuclear bodies, Nucleoplasm (IDA supported) |
| Size 蛋白大小 | 10/10 | x1 | 10 | 399 aa |
| Novelty 研究新颖性 | 10/10 | x5 | 50 | PubMed: 7 篇 |
| 3D Structure 三维结构 | 6/10 | x3 | 18 | AlphaFold pLDDT=64.7 |
| Domain 调控结构域 | 7/10 | x2 | 14 | 含 Myb/SANT 和 SWIRM 结构域，染色质结合潜力 |
| PPI Network PPI网络 | 2/10 | x3 | 6 | STRING+IntAct+GO-CC |
| Cross-validation 互证加分 | — | max +3 | +1.0 | — |
| **原始总分** |  |  | **135/183** |  |
| **归一化总分** |  |  | **73.8/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | HEK293, A-549 | HPA validated |
| UniProt | Nucleus/PML body/Cytoplasm | — |
| GO-CC | GO:0005634 Nucleus (IBA|IDA|IEA) | — |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MYPOP/IF_images/A_549_1.jpg|A-549]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MYPOP/IF_images/HEK293_1.jpg|HEK293]]
#### 3.2 蛋白大小评估

399 aa，适合生化实验和结构解析

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 7 篇 |
| 最早发表年份 | 2026 |

**主要研究方向**:
- 功能研究尚不充分，属新颖蛋白

**关键文献**:
1. Du WW et al. (2023). "Nuclear Actin Polymerization Regulates Cell Epithelial-Mesenchymal Transition.". *Adv Sci (Weinh)*. PMID: 37566765
2. Wüstenhagen E et al. (2018). "The Myb-related protein MYPOP is a novel intrinsic host restriction factor of oncogenic human papillomaviruses.". *Oncogene*. PMID: 30018400
3. Tim B et al. (2023). "Targeting of insulin receptor endocytosis as a treatment to insulin resistance.". *J Diabetes Complications*. PMID: 37788593
4. Zhao K et al. (2023). "Insight on the hub gene associated signatures and potential therapeutic agents in epilepsy and glioma.". *Brain Res Bull*. PMID: 37192718
5. Workalemahu T et al. (2017). "Genetic variations related to maternal whole blood mitochondrial DNA copy number: a genome-wide and candidate gene study.". *J Matern Fetal Neonatal Med*. PMID: 27806667


**评价**: PubMed 7 篇，属极度新颖蛋白，研究空间充足。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 64.7 |
| pLDDT > 90 占比 | 19.5% |
| pLDDT 70-90 占比 | 19.8% |
| pLDDT 50-70 占比 | 28.1% |
| pLDDT < 50 占比 | 32.6% |
| 可用 PDB 条目 | 0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MYPOP/MYPOP-PAE.png]]

**评价**: AlphaFold 预测较低质量，大部分区域无序 (AlphaFold v6, pLDDT=64.7, >90=20%, 70-90=20%, 50-70=28%, <50=33%)

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | — |

**染色质调控潜力分析**: 含 Myb/SANT 和 SWIRM 结构域，染色质结合潜力

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-2858208|uniprotkb:Q74RW5|uniprotkb:Q7CGC7|uniprotkb:A0A3N4BUB9|uniprotkb:Q0WJ85 | MI:0398(two hybrid pooling approach | PMID:imex:IM-13779|pubmed:20711500 | — | — |
| intact:EBI-2858213|ensembl:ENSP00000325402.4 | MI:0397(two hybrid array) | PMID:pubmed:32296183|imex:IM-25472 | — | — |
| intact:EBI-12868028|uniprotkb:B2RU18|ensembl:ENSP00000288861.4 | MI:1356(validated two hybrid) | PMID:pubmed:32296183|imex:IM-25472 | — | — |
| intact:EBI-740785|uniprotkb:A0A2R8Y4R9|uniprotkb:O43363|uniprotkb:B2R8U7|uniprotkb:A4D184|ensembl:ENSP00000494260.2 | MI:1356(validated two hybrid) | PMID:pubmed:32296183|imex:IM-25472 | — | — |
| intact:EBI-10172052|uniprotkb:A2RRG1|uniprotkb:Q70LJ1|uniprotkb:A6NIR9|ensembl:ENSP00000381009.3 | MI:1356(validated two hybrid) | PMID:pubmed:32296183|imex:IM-25472 | — | — |
|

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| PFN1 | 0.0 | — | — |
| BORCS7 | 0.0 | — | — |
| BORCS5 | 0.0 | — | — |
| BLOC1S1 | 0.0 | — | — |
| BORCS6 | 0.0 | — | — |
| BLOC1S2 | 0.0 | — | — |
| SNAPIN | 0.0 | — | — |
| FIZ1 | 0.0 | — | — |
|

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 复合体注释


**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 9
- 仅 IntAct 实验: 9
- 调控相关比例: 0/9 (0%)

**评价**: PPI 得分 2/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=64.7, PDB=0 | — |
| 结构域 | UniProt/InterPro | 无注释域 | — |
| PPI | STRING + IntAct + GO-CC | 9/9/0 条目 | — |
| 定位 | HPA/UniProt/GO | Nuclear bodies, Nucleoplasm / Nucleus / GO:0005634 | 一致 |

**互证加分明细**:
- GO-CC IDA 实验证据 (+0.5)
- IntAct+STRING 双源确认 (+0.5)
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ★★★ (4/5)

**核心优势**:
1. 极度新颖 (PubMed 7 篇)，几乎未被研究
2. HPA 确认核定位，高置信度

**风险/不确定性**:
1. AlphaFold 预测质量中等 (pLDDT=64.7)，部分区域无序
2. PPI 数据丰富，功能网络尚不清晰

**下一步建议**:
- [ ] 通过 IF 实验验证内源核定位
- [ ] 构建表达载体进行功能研究
- [ ] Co-IP/MS 鉴定互作蛋白

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=MYPOP
- Protein Atlas: https://www.proteinatlas.org/MYPOP
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MYPOP
- UniProt: https://www.uniprot.org/uniprotkb/Q86VE0
- SMART: http://smart.embl.de/
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86VE0


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MYPOP-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MYPOP/MYPOP-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q86VE0 |
| SMART | SM00717; |
| UniProt Domain [FT] | DOMAIN 12..84; /note="Myb-like"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00133" |
| InterPro | IPR052870;IPR028002;IPR001005; |
| Pfam | PF13873; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000176182-MYPOP/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AKAP8L | Intact | false |
| BAG4 | Intact | false |
| BBC3 | Intact | false |
| CARD10 | Intact | false |
| CHIC2 | Intact | false |
| CIB4 | Intact | false |
| CYSRT1 | Intact | false |
| FHL3 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
