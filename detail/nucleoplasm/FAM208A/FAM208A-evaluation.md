---
type: protein-evaluation
gene: "FAM208A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM208A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM208A / C3orf63, FAM208A, KIAA1105 |
| 蛋白名称 | Protein TASOR |
| 蛋白大小 | 1670 aa / 189.0 kDa |
| UniProt ID | Q9UK61 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM208A/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM208A/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 5/10 | ×1 | 5 | 1670 aa / 189.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.3; PDB: 6SWG, 6TL1 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR056242, IPR046432, IPR056243, IPR022188; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- heterochromatin (GO:0000792)
- HUSH complex (GO:0140283)
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C3orf63, FAM208A, KIAA1105 |

**关键文献**:
1. Fam208a orchestrates interaction protein network essential for early embryonic development and cell division.. *Experimental cell research*. PMID: 31112734
2. Dual role of Fam208a during zygotic cleavage and early embryonic development.. *Experimental cell research*. PMID: 34216590
3. Primate immunodeficiency virus proteins Vpx and Vpr counteract transcriptional repression of proviruses by the HUSH complex.. *Nature microbiology*. PMID: 30297740
4. Retinoblastoma-associated protein 140 as a candidate for a novel etiological gene to hypertension.. *Clinical and experimental hypertension (New York, N.Y. : 1993)*. PMID: 27391979
5. The first mouse mutants of D14Abb1e (Fam208a) show that it is critical for early development.. *Mammalian genome : official journal of the International Mammalian Genome Society*. PMID: 24781204

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.3 |
| 高置信度残基 (pLDDT>90) 占比 | 17.7% |
| 置信残基 (pLDDT 70-90) 占比 | 20.1% |
| 中等置信 (pLDDT 50-70) 占比 | 9.6% |
| 低置信 (pLDDT<50) 占比 | 52.6% |
| 有序区域 (pLDDT>70) 占比 | 37.8% |
| 可用 PDB 条目 | 6SWG, 6TL1 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM208A/FAM208A-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=56.3），有序残基占 37.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR056242, IPR046432, IPR056243, IPR022188; Pfam: PF12509, PF24630, PF23314 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PPHLN1 | 0.999 | 0.926 | — |
| MPHOSPH8 | 0.998 | 0.608 | — |
| SETDB1 | 0.822 | 0.304 | — |
| MORC2 | 0.718 | 0.000 | — |
| ZNF638 | 0.673 | 0.046 | — |
| YTHDC1 | 0.580 | 0.292 | — |
| DCAF1 | 0.503 | 0.000 | — |
| ATF7IP | 0.486 | 0.045 | — |
| USP17L19 | 0.473 | 0.000 | — |
| ATRX | 0.464 | 0.071 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TASOR | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| TBC1D4 | psi-mi:"MI:0018"(two hybrid) | pubmed:unassigned5 |
| lysS | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| asd | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| PB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28169297|imex:IM-25584 |
| KLHL40 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FAM131B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IL17RA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZNRD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.3 + PDB: 6SWG, 6TL1 | pLDDT=56.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FAM208A — Protein TASOR，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1670 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=56.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UK61
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163946-TASOR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM208A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UK61
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM208A/FAM208A-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UK61 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 166..319; /note="TASOR pseudo-PARP"; /evidence="ECO:0000269\|PubMed:33009411" |
| InterPro | IPR056242;IPR046432;IPR056243;IPR022188; |
| Pfam | PF12509;PF24630;PF23314; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000163946-TASOR/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
