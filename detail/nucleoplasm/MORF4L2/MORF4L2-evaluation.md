---
type: protein-evaluation
gene: "MORF4L2"
date: 2026-01-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MORF4L2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | MORF4L2 |
| 别名 | MRGX |
| 基因全称 | mortality factor 4 like 2 |
| 蛋白名称 | Mortality factor 4-like protein 2 |
| 蛋白大小 | 288 aa |
| UniProt ID | Q15014 |
| 评估日期 | 2026-01-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| Nucleus 核定位特异性 | 9/10 | x4 | 36 | HPA: Nucleoplasm (IDA supported) |
| Size 蛋白大小 | 10/10 | x1 | 10 | 288 aa |
| Novelty 研究新颖性 | 8/10 | x5 | 40 | PubMed: 29 篇 |
| 3D Structure 三维结构 | 7/10 | x3 | 21 | AlphaFold pLDDT=73.3 |
| Domain 调控结构域 | 7/10 | x2 | 14 | 含 MRG 结构域，参与转录调控和剪接 |
| PPI Network PPI网络 | 2/10 | x3 | 6 | STRING+IntAct+GO-CC |
| Cross-validation 互证加分 | — | max +3 | +1.0 | — |
| **原始总分** |  |  | **128/183** |  |
| **归一化总分** |  |  | **69.9/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | HeLa, MCF-7 | HPA validated |
| UniProt | Cytoplasm/Nucleus | — |
| GO-CC | GO:0005634 Nucleus (IDA|IEA|IGI|IPI) | — |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MORF4L2/IF_images/HeLa_1.jpg|HeLa]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MORF4L2/IF_images/MCF_7_1.jpg|MCF-7]]
#### 3.2 蛋白大小评估

288 aa，适合生化实验和结构解析

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 29 篇 |
| 最早发表年份 | 2026 |

**主要研究方向**:
- 功能研究尚不充分，属新颖蛋白

**关键文献**:
1. Zhang L et al. (2026). "Major depressive disorder and Hashimoto's thyroiditis: Shared immunometabolic signatures revealed by integrative transcriptomics.". *J Affect Disord*. PMID: 41365448
2. Sui XY et al. (2025). "MORF4L2 induces immunosuppressive microenvironment and immunotherapy resistance through GRHL2/MORF4L2/H4K12Ac/CSF1 axis in triple-negative breast cancer.". *Biomark Res*. PMID: 39780291
3. Devoucoux M et al. (2022). "MRG Proteins Are Shared by Multiple Protein Complexes With Distinct Functions.". *Mol Cell Proteomics*. PMID: 35636729
4. Temprano-Sagrera G et al. (2024). "Differential Expression Analyses on Human Aortic Tissue Reveal Novel Genes and Pathways Associated With Abdominal Aortic Aneurysm Onset and Progression.". *J Am Heart Assoc*. PMID: 39655704
5. Zhou X et al. (2023). "Microdeletion in distal PLP1 enhancers causes hereditary spastic paraplegia 2.". *Ann Clin Transl Neurol*. PMID: 37475517


**评价**: PubMed 29 篇，属非常新颖蛋白，研究空间充足。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 73.3 |
| pLDDT > 90 占比 | 48.3% |
| pLDDT 70-90 占比 | 8.7% |
| pLDDT 50-70 占比 | 13.2% |
| pLDDT < 50 占比 | 29.9% |
| 可用 PDB 条目 | 0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MORF4L2/MORF4L2-PAE.png]]

**评价**: AlphaFold 预测中等质量，部分区域有序 (AlphaFold v6, pLDDT=73.3, >90=48%, 70-90=9%, 50-70=13%, <50=30%)

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | — |

**染色质调控潜力分析**: 含 MRG 结构域，参与转录调控和剪接

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-399076|uniprotkb:A8C4L5|ensembl:ENSP00000359518.3 | MI:0007(anti tag coimmunoprecipitat | PMID:pubmed:12963728 | — | — |
| intact:EBI-355018|uniprotkb:Q8TAE5|uniprotkb:Q9BVS8|uniprotkb:Q9H0W6|uniprotkb:B3KMN1|uniprotkb:D3DNR9|ensembl:ENSP00000397552.2 | MI:0071(molecular sieving) | PMID:pubmed:12963728 | — | — |
| intact:EBI-769266|uniprotkb:O43178|uniprotkb:Q15355|uniprotkb:Q58AB0|uniprotkb:Q59GN0|uniprotkb:Q969M9|intact:EBI-28979295|ensembl:ENSP00000254900.5 | MI:0401(biochemical) | PMID:pubmed:12963728 | — | — |
| intact:EBI-1181367|uniprotkb:Q13977|uniprotkb:A8K8A8|ensembl:ENSP00000268383.2 | MI:0018(two hybrid) | PMID:pubmed:11988016|imex:IM-19508 | — | — |
| intact:EBI-399257|uniprotkb:B3KP92|uniprotkb:Q567V0|uniprotkb:Q8J026|uniprotkb:D3DXA5|ensembl:ENSP00000353643.1|ensembl:ENSP00000391969.2|ensembl:ENSP00000410532.1|ensembl:ENSP00000415476.2 | MI:0018(two hybrid) | PMID:pubmed:11988016|imex:IM-19508 | — | — |
|

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| MRGBP | 0.0 | — | — |
| TRRAP | 0.0 | — | — |
| KAT5 | 0.0 | — | — |
| YEATS4 | 0.0 | — | — |
| BRD8 | 0.0 | — | — |
| MORF4L1 | 0.0 | — | — |
| MEAF6 | 0.0 | — | — |
| DMAP1 | 0.0 | — | — |
|

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 复合体注释


**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 15
- 仅 IntAct 实验: 11
- 调控相关比例: 1/15 (7%)

**评价**: PPI 得分 2/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=73.3, PDB=0 | — |
| 结构域 | UniProt/InterPro | 无注释域 | — |
| PPI | STRING + IntAct + GO-CC | 15/11/0 条目 | — |
| 定位 | HPA/UniProt/GO | Nucleoplasm / Nucleus / GO:0005634 | 一致 |

**互证加分明细**:
- GO-CC IDA 实验证据 (+0.5)
- IntAct+STRING 双源确认 (+0.5)
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ★★ (3/5)

**核心优势**:
1. 非常新颖 (PubMed 29 篇)，几乎未被研究
2. HPA 确认核定位，高置信度

**风险/不确定性**:
1. AlphaFold 结构预测置信度较高
2. PPI 数据丰富，功能网络尚不清晰

**下一步建议**:
- [ ] 通过 IF 实验验证内源核定位
- [ ] 构建表达载体进行功能研究
- [ ] Co-IP/MS 鉴定互作蛋白

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=MORF4L2
- Protein Atlas: https://www.proteinatlas.org/MORF4L2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MORF4L2
- UniProt: https://www.uniprot.org/uniprotkb/Q15014
- SMART: http://smart.embl.de/
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15014


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MORF4L2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MORF4L2/MORF4L2-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q15014 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 117..288; /note="MRG"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00972" |
| InterPro | IPR008676;IPR038217;IPR026541; |
| Pfam | PF05712; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000123562-MORF4L2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ACTL6A | Intact, Biogrid | true |
| BRD8 | Intact, Biogrid | true |
| CDR2 | Intact, Biogrid | true |
| DMAP1 | Biogrid, Bioplex | true |
| MRFAP1 | Intact, Biogrid, Bioplex | true |
| MRFAP1L1 | Intact, Biogrid, Bioplex | true |
| MRGBP | Intact, Biogrid, Bioplex | true |
| PALB2 | Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
