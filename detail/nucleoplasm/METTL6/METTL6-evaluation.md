---
type: protein-evaluation
gene: "METTL6"
date: 2026-01-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## METTL6 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | METTL6 |
| 别名 | — |
| 基因全称 | methyltransferase 6 |
| 蛋白名称 | tRNA N(3)-cytidine methyltransferase METTL6 |
| 蛋白大小 | 284 aa |
| UniProt ID | Q8TCB7 |
| 评估日期 | 2026-01-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| Nucleus 核定位特异性 | 4/10 | x4 | 16 | HPA: Nucleoplasm |
| Size 蛋白大小 | 10/10 | x1 | 10 | 284 aa |
| Novelty 研究新颖性 | 10/10 | x5 | 50 | PubMed: 20 篇 |
| 3D Structure 三维结构 | 10/10 | x3 | 30 | AlphaFold pLDDT=91.9 |
| Domain 调控结构域 | 7/10 | x2 | 14 | 含甲基转移酶结构域，可能参与表观遗传调控 |
| PPI Network PPI网络 | 2/10 | x3 | 6 | STRING+IntAct+GO-CC |
| Cross-validation 互证加分 | — | max +3 | +1.5 | — |
| **原始总分** |  |  | **127.5/183** |  |
| **归一化总分** |  |  | **69.7/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | U-251MG, A-431 | HPA validated |
| UniProt |  | — |
| GO-CC | GO:0005634 Nucleus (IBA|IEA) | — |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/METTL6/IF_images/A_431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/METTL6/IF_images/U_251MG_1.jpg|U-251MG]]
#### 3.2 蛋白大小评估

284 aa，适合生化实验和结构解析

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 20 篇 |
| 最早发表年份 | 2025 |

**主要研究方向**:
- 功能研究尚不充分，属新颖蛋白

**关键文献**:
1. Cui J et al. (2024). "m(3)C32 tRNA modification controls serine codon-biased mRNA translation, cell cycle, and DNA-damage response.". *Nat Commun*. PMID: 38982125
2. Throll P et al. (2024). "Structural basis of tRNA recognition by the m(3)C RNA methyltransferase METTL6 in complex with SerRS seryl-tRNA synthetase.". *Nat Struct Mol Biol*. PMID: 38918637
3. Tooley JG et al. (2023). "METTLing in Stem Cell and Cancer Biology.". *Stem Cell Rev Rep*. PMID: 36094754
4. Li S et al. (2022). "Structural basis for METTL6-mediated m3C RNA methylation.". *Biochem Biophys Res Commun*. PMID: 34922197
5. Zhou X et al. (2024). "Mitochondrial RNA modification-based signature to predict prognosis of lower grade glioma: a multi-omics exploration and verification study.". *Sci Rep*. PMID: 38824202


**评价**: PubMed 20 篇，属极度新颖蛋白，研究空间充足。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 91.9 |
| pLDDT > 90 占比 | 80.3% |
| pLDDT 70-90 占比 | 12.3% |
| pLDDT 50-70 占比 | 2.5% |
| pLDDT < 50 占比 | 4.9% |
| 可用 PDB 条目 | 7 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/METTL6/METTL6-PAE.png]]

**评价**: AlphaFold 预测高质量，整体折叠良好 (AlphaFold v6, pLDDT=91.9, >90=80%, 70-90=12%, 50-70=2%, <50=5%. PDB entries: 7EZG, 7F1E, 8OWX, 8OWY, 8P7B)

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | — |

**染色质调控潜力分析**: 含甲基转移酶结构域，可能参与表观遗传调控

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-751540|uniprotkb:B0UXA2|uniprotkb:A6NG25|uniprotkb:Q5SQ49|ensembl:ENSP00000211377.3|ensembl:ENSP00000365057.2|ensembl:ENSP00000365059.2|ensembl:ENSP00000365060.4|ensembl:ENSP00000365065.4|ensembl:ENSP00000365071.1|ensembl:ENSP00000372926.2|ensembl:ENSP00000372928.4|ensembl:ENSP00000382994.3|ensembl:ENSP00000382999.1|ensembl:ENSP00000383005.1|ensembl:ENSP00000389339.2|ensembl:ENSP00000390746.1|ensembl:ENSP00000391604.1|ensembl:ENSP00000393567.2|ensembl:ENSP00000398927.2|ensembl:ENSP00000399890.1|ensembl:ENSP00000401272.1|ensembl:ENSP00000401276.1|ensembl:ENSP00000401376.1|ensembl:ENSP00000403829.2|ensembl:ENSP00000406507.1|ensembl:ENSP00000406895.2|ensembl:ENSP00000409206.1|ensembl:ENSP00000410690.2|ensembl:ENSP00000411691.1|ensembl:ENSP00000412321.2|ensembl:ENSP00000412884.1|ensembl:ENSP00000413662.1|ensembl:ENSP00000415855.2 | MI:1356(validated two hybrid) | PMID:pubmed:32296183|imex:IM-25472 | — | — |
| intact:EBI-17861723|ensembl:ENSP00000373300.3|ensembl:ENSP00000407613.1|uniprotkb:Q96LU4 | MI:0007(anti tag coimmunoprecipitat | PMID:pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | — | — |
|

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| TSR3 | 0.0 | — | — |
| NSUN5 | 0.0 | — | — |
| SARS1 | 0.0 | — | — |
| SARS2 | 0.0 | — | — |
| SARS2-2 | 0.0 | — | — |
| TRMT10B | 0.0 | — | — |
| EAF1 | 0.0 | — | — |
| DALRD3 | 0.0 | — | — |
|

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 复合体注释


**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 15
- 仅 IntAct 实验: 2
- 调控相关比例: 0/15 (0%)

**评价**: PPI 得分 2/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=91.9, PDB=7 | — |
| 结构域 | UniProt/InterPro | 无注释域 | — |
| PPI | STRING + IntAct + GO-CC | 15/2/0 条目 | — |
| 定位 | HPA/UniProt/GO | Nucleoplasm / Nucleus / GO:0005634 | 一致 |

**互证加分明细**:
- PDB+AlphaFold 双源确认 (+0.5)
- IntAct+STRING 双源确认 (+0.5)
- PDB 多条目 (>=3) (+0.5)
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ★★ (3/5)

**核心优势**:
1. 极度新颖 (PubMed 20 篇)，几乎未被研究
2. HPA 确认核定位，中等置信度

**风险/不确定性**:
1. AlphaFold 结构预测置信度较高
2. PPI 数据丰富，功能网络尚不清晰

**下一步建议**:
- [ ] 通过 IF 实验验证内源核定位
- [ ] 构建表达载体进行功能研究
- [ ] Co-IP/MS 鉴定互作蛋白

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=METTL6
- Protein Atlas: https://www.proteinatlas.org/METTL6
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=METTL6
- UniProt: https://www.uniprot.org/uniprotkb/Q8TCB7
- SMART: http://smart.embl.de/
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TCB7


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[METTL6-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/METTL6/METTL6-PAE.png]]




