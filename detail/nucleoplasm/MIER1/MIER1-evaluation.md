---
type: protein-evaluation
gene: "MIER1"
date: 2026-01-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MIER1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | MIER1 |
| 别名 | MI-ER1, hMI-ER1 |
| 基因全称 | MIER1 transcriptional regulator |
| 蛋白名称 | Mesoderm induction early response protein 1 |
| 蛋白大小 | 512 aa |
| UniProt ID | Q8N108 |
| 评估日期 | 2026-01-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| Nucleus 核定位特异性 | 8/10 | x4 | 32 | HPA: Nucleoplasm |
| Size 蛋白大小 | 10/10 | x1 | 10 | 512 aa |
| Novelty 研究新颖性 | 8/10 | x5 | 40 | PubMed: 23 篇 |
| 3D Structure 三维结构 | 6/10 | x3 | 18 | AlphaFold pLDDT=61.9 |
| Domain 调控结构域 | 7/10 | x2 | 14 | 无已注释染色质调控结构域 |
| PPI Network PPI网络 | 8/10 | x3 | 24 | STRING+IntAct+GO-CC |
| Cross-validation 互证加分 | — | max +3 | +0.5 | — |
| **原始总分** |  |  | **138.5/183** |  |
| **归一化总分** |  |  | **75.7/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | U-251MG, A-431 | HPA validated |
| UniProt | Nucleus | — |
| GO-CC | GO:0005634 Nucleus (IBA|IEA) | — |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MIER1/IF_images/A_431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MIER1/IF_images/U_251MG_1.jpg|U-251MG]]
#### 3.2 蛋白大小评估

512 aa，适合生化实验和结构解析

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 23 篇 |
| 最早发表年份 | 2026 |

**主要研究方向**:
- 功能研究尚不充分，属新颖蛋白

**关键文献**:
1. Ding Q et al. (2024). "Integrated analysis of single-cell RNA-seq, bulk RNA-seq, Mendelian randomization, and eQTL reveals T cell-related nomogram model and subtype classification in rheumatoid arthritis.". *Front Immunol*. PMID: 38962008
2. Chen Y et al. (2023). "Acute liver steatosis translationally controls the epigenetic regulator MIER1 to promote liver regeneration in a study with male mice.". *Nat Commun*. PMID: 36934083
3. Xiong J et al. (2024). "Acute liver steatosis signals the chromatin for regeneration via MIER1.". *Metabol Open*. PMID: 39351485
4. Wei ZY et al. (2024). "Bulk and single-cell RNA-seq analyses reveal canonical RNA editing associated with microglia homeostasis and its role in sepsis-associated encephalopathy.". *Neuroscience*. PMID: 39293730
5. Wang S et al. (2023). "A potential histone-chaperone activity for the MIER1 histone deacetylase complex.". *Nucleic Acids Res*. PMID: 37099381


**评价**: PubMed 23 篇，属非常新颖蛋白，研究空间充足。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 61.9 |
| pLDDT > 90 占比 | 17.6% |
| pLDDT 70-90 占比 | 18.8% |
| pLDDT 50-70 占比 | 20.5% |
| pLDDT < 50 占比 | 43.2% |
| 可用 PDB 条目 | 0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MIER1/MIER1-PAE.png]]

**评价**: AlphaFold 预测较低质量，大部分区域无序 (AlphaFold v6, pLDDT=61.9, >90=18%, 70-90=19%, 50-70=20%, <50=43%)

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | — |

**染色质调控潜力分析**: 无已注释染色质调控结构域

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-1387386|uniprotkb:Q0VDG7|uniprotkb:Q32NC5|uniprotkb:Q5VX99|uniprotkb:Q6P7T5|uniprotkb:Q9BWZ2|uniprotkb:Q9Y424|uniprotkb:A8K6D6|uniprotkb:B4DLG4|ensembl:ENSP00000330512.5 | MI:0006(anti bait coimmunoprecipita | PMID:pubmed:21258344|imex:IM-17039 | — | — |
| intact:EBI-744366|uniprotkb:B0UZY2|uniprotkb:Q14349|uniprotkb:Q6PK06|uniprotkb:Q96MH5|uniprotkb:Q96QD0|uniprotkb:Q9UQL8|uniprotkb:Q9Y331|uniprotkb:Q5JQ92|uniprotkb:Q5JP83|uniprotkb:Q5JQA1|uniprotkb:Q5JQG3|ensembl:ENSP00000364687.4|ensembl:ENSP00000372864.4|ensembl:ENSP00000392305.2|ensembl:ENSP00000396119.2|ensembl:ENSP00000406110.2|ensembl:ENSP00000416957.2 | MI:0006(anti bait coimmunoprecipita | PMID:pubmed:21258344|imex:IM-17039 | — | — |
| intact:EBI-301834|uniprotkb:Q92534|ensembl:ENSP00000362649.3 | MI:0006(anti bait coimmunoprecipita | PMID:pubmed:21258344|imex:IM-17039 | — | — |
| intact:EBI-301821|uniprotkb:Q5SRI8|uniprotkb:Q5SZ86|uniprotkb:Q8NEH4|uniprotkb:B4DL58|uniprotkb:E1P561|uniprotkb:B3KRS5|ensembl:ENSP00000430432.1 | MI:0006(anti bait coimmunoprecipita | PMID:pubmed:21258344|imex:IM-17039 | — | — |
| intact:EBI-8637742|ensembl:ENSP00000319141.4|uniprotkb:Q6KC16|uniprotkb:Q6P147|uniprotkb:Q6ZR51|uniprotkb:Q9H0Q8|intact:MINT-8162723|uniprotkb:Q9H5G5|uniprotkb:B2RE79|uniprotkb:Q6KC17|uniprotkb:B4DWD7|intact:EBI-10977751 | MI:0007(anti tag coimmunoprecipitat | PMID:pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | — | — |
|

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| HDAC1 | 0.0 | — | — |
| HDAC2 | 0.0 | — | — |
| CDYL | 0.0 | — | — |
| ESR1 | 0.0 | — | — |
| CYBRD1 | 0.0 | — | — |
| C16orf87 | 0.0 | — | — |
| EHMT2 | 0.0 | — | — |
| H2AZ1 | 0.0 | — | — |
|

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 复合体注释


**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 15
- 仅 IntAct 实验: 17
- 调控相关比例: 4/15 (27%)

**评价**: PPI 得分 8/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=61.9, PDB=0 | — |
| 结构域 | UniProt/InterPro | 无注释域 | — |
| PPI | STRING + IntAct + GO-CC | 15/17/0 条目 | — |
| 定位 | HPA/UniProt/GO | Nucleoplasm / Nucleus / GO:0005634 | 一致 |

**互证加分明细**:
- IntAct+STRING 双源确认 (+0.5)
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ★★★ (4/5)

**核心优势**:
1. 非常新颖 (PubMed 23 篇)，几乎未被研究
2. HPA 确认核定位，高置信度

**风险/不确定性**:
1. AlphaFold 预测质量中等 (pLDDT=61.9)，部分区域无序
2. PPI 数据丰富，功能网络尚不清晰

**下一步建议**:
- [ ] 通过 IF 实验验证内源核定位
- [ ] 构建表达载体进行功能研究
- [ ] Co-IP/MS 鉴定互作蛋白

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=MIER1
- Protein Atlas: https://www.proteinatlas.org/MIER1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MIER1
- UniProt: https://www.uniprot.org/uniprotkb/Q8N108
- SMART: http://smart.embl.de/
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N108


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MIER1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MIER1/MIER1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8N108 |
| SMART | SM01189;SM00717; |
| UniProt Domain [FT] | DOMAIN 180..278; /note="ELM2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00512"; DOMAIN 283..335; /note="SANT"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00624" |
| InterPro | IPR000949;IPR009057;IPR040138;IPR045787;IPR001005;IPR017884; |
| Pfam | PF01448;PF19426;PF00249; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000198160-MIER1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HDAC1 | Intact, Biogrid, Opencell | true |
| HDAC2 | Biogrid, Opencell | true |
| CDYL | Biogrid | false |
| H2AX | Biogrid | false |
| H2AZ1 | Biogrid | false |
| H2BC8 | Biogrid | false |
| SOX2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
