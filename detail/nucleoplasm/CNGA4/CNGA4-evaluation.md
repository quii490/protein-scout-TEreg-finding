---
type: protein-evaluation
gene: "CNGA4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CNGA4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CNGA4 |
| 蛋白名称 | Cyclic nucleotide-gated channel alpha-4 |
| 蛋白大小 | 575 aa / 66.0 kDa |
| UniProt ID | Q8IV77 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Plasma membrane; UniProt: Cell projection, cilium membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 575 aa / 66.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.5; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR032406, IPR050866, IPR018488, IPR000595, IPR018 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane | Uncertain |
| UniProt | Cell projection, cilium membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- ciliary membrane (GO:0060170)
- Golgi-associated vesicle membrane (GO:0030660)
- intracellular cyclic nucleotide activated cation channel complex (GO:0017071)
- non-motile cilium membrane (GO:0098804)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 32 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Importance of the CNGA4 channel gene for odor discrimination and adaptation in behaving mice.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 12649326
2. Neuron-non-neuron electrical coupling networks are involved in chronic stress-induced electrophysiological changes in lateral habenular neurons.. *The Journal of physiology*. PMID: 40168081
3. Loss of CNGB1 protein leads to olfactory dysfunction and subciliary cyclic nucleotide-gated channel trapping.. *The Journal of biological chemistry*. PMID: 16980309
4. Comparative Gene Signature of Nociceptors Innervating Mouse Molar Teeth, Cranial Meninges, and Cornea.. *Anesthesia and analgesia*. PMID: 38236765
5. Central role of the CNGA4 channel subunit in Ca2+-calmodulin-dependent odor adaptation.. *Science (New York, N.Y.)*. PMID: 11739959

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.5 |
| 高置信度残基 (pLDDT>90) 占比 | 45.6% |
| 置信残基 (pLDDT 70-90) 占比 | 41.9% |
| 中等置信 (pLDDT 50-70) 占比 | 2.8% |
| 低置信 (pLDDT<50) 占比 | 9.7% |
| 有序区域 (pLDDT>70) 占比 | 87.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=83.5，有序区 87.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR032406, IPR050866, IPR018488, IPR000595, IPR018490; Pfam: PF16526, PF00027, PF00520 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CNGB1 | 0.999 | 0.297 | — |
| CNGA2 | 0.998 | 0.000 | — |
| CALM3 | 0.970 | 0.000 | — |
| CALML4 | 0.969 | 0.000 | — |
| CALML3 | 0.969 | 0.000 | — |
| CALML6 | 0.969 | 0.000 | — |
| CALML5 | 0.969 | 0.000 | — |
| CNGB3 | 0.864 | 0.297 | — |
| ADCY3 | 0.815 | 0.047 | — |
| ANO2 | 0.806 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CCDC22 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SNAPIN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SNAP29 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CORO1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ATP1A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ITPR3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ERMP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| COMMD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LRRC8A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GHDC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.5 + PDB: 无 | pLDDT=83.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, cilium membrane / Nucleoplasm, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CNGA4 — Cyclic nucleotide-gated channel alpha-4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小575 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IV77
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132259-CNGA4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CNGA4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IV77
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
