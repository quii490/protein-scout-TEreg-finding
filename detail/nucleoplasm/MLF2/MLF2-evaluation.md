---
type: protein-evaluation
gene: "MLF2"
date: 2026-01-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MLF2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | MLF2 |
| 别名 | NTN4 |
| 基因全称 | myeloid leukemia factor 2 |
| 蛋白名称 | Myeloid leukemia factor 2 |
| 蛋白大小 | 248 aa |
| UniProt ID | Q15773 |
| 评估日期 | 2026-01-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| Nucleus 核定位特异性 | 8/10 | x4 | 32 | HPA: Nucleoplasm |
| Size 蛋白大小 | 10/10 | x1 | 10 | 248 aa |
| Novelty 研究新颖性 | 8/10 | x5 | 40 | PubMed: 29 篇 |
| 3D Structure 三维结构 | 7/10 | x3 | 21 | AlphaFold pLDDT=65.1 |
| Domain 调控结构域 | 7/10 | x2 | 14 | 无已注释染色质调控结构域 |
| PPI Network PPI网络 | 8/10 | x3 | 24 | STRING+IntAct+GO-CC |
| Cross-validation 互证加分 | — | max +3 | +0.5 | — |
| **原始总分** |  |  | **141.5/183** |  |
| **归一化总分** |  |  | **77.3/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | U-251MG, A-431 | HPA validated |
| UniProt | Nucleus | — |
| GO-CC | GO:0005634 Nucleus (IBA|IEA) | — |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MLF2/IF_images/A_431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MLF2/IF_images/U_251MG_1.jpg|U-251MG]]
#### 3.2 蛋白大小评估

248 aa，适合生化实验和结构解析

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 29 篇 |
| 最早发表年份 | 2026 |

**主要研究方向**:
- 功能研究尚不充分，属新颖蛋白

**关键文献**:
1. Zeng C et al. (2025). "PIM3-mediated phosphorylation stabilizes myeloid leukemia factor 2 to promote metastasis in osteosarcoma.". *J Clin Invest*. PMID: 41090348
2. Schwaemmle H et al. (2025). "CRISPR screen decodes SWI/SNF chromatin remodeling complex assembly.". *Nat Commun*. PMID: 40447637
3. Poch D et al. (2025). "Integrative Chemical Genetics Platform Identifies Condensate Modulators Linked to Neurological Disorders.". *bioRxiv*. PMID: 40502095
4. Huang D et al. (2020). "CRL4(DCAF8) and USP11 oppositely regulate the stability of myeloid leukemia factors (MLFs).". *Biochem Biophys Res Commun*. PMID: 32703400
5. Deng C et al. (2025). "Multi-omics analysis identifies diagnostic circulating biomarkers and potential therapeutic targets, revealing IQGAP1 as an oncogene in gastric cancer.". *NPJ Precis Oncol*. PMID: 40229327


**评价**: PubMed 29 篇，属非常新颖蛋白，研究空间充足。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 65.1 |
| pLDDT > 90 占比 | 26.2% |
| pLDDT 70-90 占比 | 19.4% |
| pLDDT 50-70 占比 | 15.7% |
| pLDDT < 50 占比 | 38.7% |
| 可用 PDB 条目 | 0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MLF2/MLF2-PAE.png]]

**评价**: AlphaFold 预测中等质量，部分区域有序 (AlphaFold v6, pLDDT=65.1, >90=26%, 70-90=19%, 50-70=16%, <50=39%)

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | — |

**染色质调控潜力分析**: 无已注释染色质调控结构域

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-602878|uniprotkb:A2A5D1|uniprotkb:B7ZC17|ensembl:ENSMUSP00000120152.2 | MI:0018(two hybrid) | PMID:pubmed:15102471 | — | — |
| intact:EBI-1051875|intact:EBI-9357094|ensembl:ENSP00000203630.5|ensembl:ENSP00000403941.1|ensembl:ENSP00000446317.1 | MI:0006(anti bait coimmunoprecipita | PMID:pubmed:17353931 | — | — |
| intact:EBI-1053164|uniprotkb:A4D232|uniprotkb:O95806|uniprotkb:A8KAG0|uniprotkb:B4DN73|uniprotkb:E9PCZ2|uniprotkb:Q53EN8|uniprotkb:Q59EF2|uniprotkb:Q6FIC8|uniprotkb:Q75MA2|uniprotkb:Q9UIK6|uniprotkb:A8K7D8|ensembl:ENSP00000262177.4 | MI:0399(two hybrid fragment pooling | PMID:pubmed:23414517|imex:IM-16425 | — | — |
| intact:EBI-2812936|uniprotkb:Q6HU26|uniprotkb:Q81MM9 | MI:0398(two hybrid pooling approach | PMID:imex:IM-13779|pubmed:20711500 | — | — |
| intact:EBI-1383852|uniprotkb:Q9H1E8|uniprotkb:Q9UD43|ensembl:ENSP00000360290.4 | MI:0007(anti tag coimmunoprecipitat | PMID:pubmed:20562859|imex:IM-15184 | — | — |
|

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| DNAJB6 | 0.0 | — | — |
| ARFGAP2 | 0.0 | — | — |
| SCGN | 0.0 | — | — |
| CROCC | 0.0 | — | — |
| DNAJB1 | 0.0 | — | — |
| DNAJB4 | 0.0 | — | — |
| STUB1 | 0.0 | — | — |
| DOC2A | 0.0 | — | — |
|

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 复合体注释


**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 15
- 仅 IntAct 实验: 9
- 调控相关比例: 6/15 (40%)

**评价**: PPI 得分 8/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=65.1, PDB=0 | — |
| 结构域 | UniProt/InterPro | 无注释域 | — |
| PPI | STRING + IntAct + GO-CC | 15/9/0 条目 | — |
| 定位 | HPA/UniProt/GO | Nucleoplasm / Nucleus / GO:0005634 | 一致 |

**互证加分明细**:
- IntAct+STRING 双源确认 (+0.5)
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ★★★ (4/5)

**核心优势**:
1. 非常新颖 (PubMed 29 篇)，几乎未被研究
2. HPA 确认核定位，高置信度

**风险/不确定性**:
1. AlphaFold 预测质量中等 (pLDDT=65.1)，部分区域无序
2. PPI 数据丰富，功能网络尚不清晰

**下一步建议**:
- [ ] 通过 IF 实验验证内源核定位
- [ ] 构建表达载体进行功能研究
- [ ] Co-IP/MS 鉴定互作蛋白

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=MLF2
- Protein Atlas: https://www.proteinatlas.org/MLF2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MLF2
- UniProt: https://www.uniprot.org/uniprotkb/Q15773
- SMART: http://smart.embl.de/
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15773


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MLF2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MLF2/MLF2-PAE.png]]




