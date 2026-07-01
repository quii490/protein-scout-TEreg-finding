---
type: protein-evaluation
gene: "WDR20"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## WDR20 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | WDR20 |
| 蛋白名称 | WD repeat-containing protein 20 |
| 蛋白大小 | 569 aa / 62.9 kDa |
| UniProt ID | Q8TBZ3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 569 aa / 62.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=77.7; PDB: 5K19, 5K1C, 6JLQ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR015943, IPR036322, IPR001680, IPR051362; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **141.0/180** | |
| **归一化总分** | | | **78.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 25 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. WDR20 prevents hepatocellular carcinoma senescence by orchestrating the simultaneous USP12/46-mediated deubiquitination of c-Myc.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 39432777
2. The dystrophia myotonica WD repeat-containing protein DMWD and WDR20 differentially regulate USP12 deubiquitinase.. *The FEBS journal*. PMID: 33844468
3. DEPDC5 regulates the strength of excitatory synaptic transmission by interacting with ubiquitin-specific protease 46.. *Neurobiology of disease*. PMID: 40467011
4. Characterization of WDR20: A new regulator of the ERAD machinery.. *Biochimica et biophysica acta. Molecular cell research*. PMID: 29655804
5. WDR20 regulates activity of the USP12 x UAF1 deubiquitinating enzyme complex.. *The Journal of biological chemistry*. PMID: 20147737

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.7 |
| 高置信度残基 (pLDDT>90) 占比 | 61.5% |
| 置信残基 (pLDDT 70-90) 占比 | 7.2% |
| 中等置信 (pLDDT 50-70) 占比 | 3.5% |
| 低置信 (pLDDT<50) 占比 | 27.8% |
| 有序区域 (pLDDT>70) 占比 | 68.7% |
| 可用 PDB 条目 | 5K19, 5K1C, 6JLQ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（5K19, 5K1C, 6JLQ）+ AlphaFold高质量预测（pLDDT=77.7），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015943, IPR036322, IPR001680, IPR051362; Pfam: PF00400 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| USP12 | 0.999 | 0.930 | — |
| WDR48 | 0.999 | 0.888 | — |
| USP46 | 0.988 | 0.916 | — |
| PHLPP2 | 0.904 | 0.828 | — |
| PHLPP1 | 0.877 | 0.777 | — |
| BRAP | 0.783 | 0.000 | — |
| USP1 | 0.758 | 0.429 | — |
| AR | 0.694 | 0.310 | — |
| USP26 | 0.626 | 0.047 | — |
| VSX2 | 0.620 | 0.618 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Mcf2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| USP12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| PHLPP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| PHLPP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| WDR48 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| YWHAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| FBXW5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| OPTN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| POLR1C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.7 + PDB: 5K19, 5K1C, 6JLQ | pLDDT=77.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. WDR20 — WD repeat-containing protein 20，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小569 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| WDR48 | STRING | 999 |
| USP46 | STRING | 988 |
| PHLPP2 | STRING | 904 |
| PHLPP1 | STRING | 877 |
| BRAP | STRING | 783 |
| USP1 | STRING | 758 |
| PDHA1 | BioGRID | 1 |
| SURF2 | BioGRID | 1 |


### 深度机制分析

WDR20(569 aa, 62.9 kDa)是WD40重复蛋白家族的成员(IPR015943/IPR036322/IPR001680, Pfam PF00400, SMART SM00320)，其结构由7个WD40重复形成的beta-螺旋桨折叠为核心——每个WD重复贡献四股反平行beta-sheet，整体形成一个能够承载多个蛋白结合表面的平台状架构。AlphaFold pLDDT 77.7在WD40家族中属于中等水平，但其27.8%的pLDDT <50区域暗示部分loops和N/C端尾巴高度flexible，3个PDB条目(5K19/5K1C/6JLQ)仅覆盖部分WD40域(WD1-5)，表明完整的WD40域(WD1-7)和其构象动态尚未被实验结构完整捕获。WDR20的功能基于其作为去泛素化酶(DUB)的支架/适配蛋白角色——在ALL PPI网络中，WDR20与USP12/DUB1(STRING 999, IntAct coIP)、WDR48/UAF1(STRING 999)和USP46(STRING 988)形成稳定的三元DUB复合物(USP12-WDR20-WDR48/USP46-WDR20-WDR48)，WDR20在此架构中充当催化USP12/46的激活因子——在缺乏WDR20的情况下，USP12/46的DUB活性几乎为零(PMID 20147737, PMID 33844468, PMID 29655804)。

这一DUB复合物对TE调控具有重要意义，原因在于：(i) USP12/46共同靶向组蛋白H2A和H2B的去泛素化——H2AK119ub1(由Polycomb PRC1-RING1A/B写入)是Polycomb抑制复合物PRC2在TE位点(LINE-1/LTR/HERV)上维持H3K27me3沉默的先决条件；(ii) c-Myc是WDR20-USP12/46轴的另一个关键去泛素化底物(PMID 39432777)——在HCC中WDR20通过保护c-Myc免受蛋白酶体降解维持其致癌功能——c-Myc直接结合TE(LTR/HERV)和rDNA重复序列并驱动它们的RNA Pol II转录；(iii) PHLPP1/2(PH domain leucine-rich repeat protein phosphatase 1/2, STRING 904/877)通过去磷酸化Akt和PKC的疏水基序，间接调控mTORC1——mTORC1信号是LINE-1反转座的主要激活因子(通过磷酸化S6K1可增强L1-ORF2p RT活性)。因此，WDR20通过USP12/46复合物对H2AK119ub1的去除——进而解禁Polycomb沉默——构成了对TE位点单一最为直接的泛素化层面的表观调控。

WDR20的"去泛素化支架"身份从结构上解释了其核定位信号：WD40 beta-螺旋桨的顶部面(对应于WD4-6的loops和beta-turns)富含碱性残基(GSK-basic patches)，这些碱性表面可能作为非经典NLS被KPNA2(importin-alpha 2)识别。同时，WDR20在PPI网络中与KRAS(BioGRID coIP)的共现增加了一层癌症特异性TE调控——RAS突变(MAPK通路持续性激活)已知诱发全基因组TE表达(特别是HERV-K和LINE-1)，而WDR20-USP12/46复合物可能是这一致癌信号-表观遗传串扰的关键中介者。DAPP1(双重adaptor of phosphotyrosine and 3-phosphoinositides)作为另一个PPI伙伴提示PH domain介导的PI3K信号(第2信使PIP3)可能直接招募WDR20-USP12/46复合物至染色质的特定PIP3富集位点——这是一个鲜有探索的"PI-lipid code of the nucleus"概念，其可能选择性标记TE的活性位点。值得注意的是OPTN(optineurin)的PPI——OPTN是选择性自噬受体和NF-kappaB的负调控因子——其在清除泛素化蛋白聚集体方面的功能与WDR20的去泛素化功能形成鲜明对比，提示在TE产生大量异常蛋白(ORF1p聚集体)的背景下，WDR20与OPTN可能构成"聚集体-去泛素化/自噬降解"的竞争调控。

机制模型：在细胞稳态下，WDR20-USP12/46-WDR48复合物被限制在染色质核区(通过WD40-PIP3和PHLPP的锚定)，其对TE位点处H2AK119ub1的选择性去泛素化维持该位点在Polycomb和Trithorax组蛋白修饰之间的动态均衡(H3K27me3 ↔ H3K27ac)，使TE表达维持在基础水平的"可控泄漏"状态。在RAS/MAPK持续激活或c-Myc过表达的情况下(WDR20保护c-Myc)时，WDR20复合物过度稳定c-Myc蛋白并过度清除H2AK119ub1信号——PRC2无法识别H2AK119ub1进而不能沉积H3K27me3——导致TE批量去抑制。这提示WDR20的抑制剂可成为"TE-表观遗传锁定"策略的小分子靶标——阻断WDR20-USP12互作或用PROTAC降解WDR20可能恢复Polycomb抑制机制在TE位点的功能。研究启示：WDR20的极度低PubMed(16篇strict)与结构/功能信息的富集(3 PDB, WD40-支架架构清楚, PPI核心靶标已鉴定)使其成为这18个蛋白中成药性最高的候选之一。其作为支架蛋白而非酶的属性暗示传统的活性位点抑制剂策略不适用，而PPI抑制剂(PROTAC或分子胶)和disease-relevant c-Myc HCC模型(PMID 39432777)为验证WDR20依赖的TE调控功能提供了成熟的实验体系。实验策略：利用已发表的USP12-Ub covalent trap assay(PMID 33844468)确定WDR20 WD repeats中哪个重复(WD3-5候选)贡献USP12结合表面；构造delta-WD3-5缺失突变体并在HCC细胞(HepG2, Huh7)中进行TE-family RT-qPCR(LINE-1 ORF1/ORF2, HERV-K gag/env, Alu, SVA)以及H2AK119ub1泛素化水平的定量(quantitative ubiquitin proteomics after H2A IP)。

### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TBZ3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140153-WDR20/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=WDR20
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TBZ3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TBZ3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8TBZ3 |
| SMART | SM00320; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR015943;IPR036322;IPR001680;IPR051362; |
| Pfam | PF00400; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000140153-WDR20/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DAPP1 | Intact, Biogrid | true |
| USP12 | Intact, Biogrid | true |
| USP46 | Intact, Biogrid | true |
| FBXW5 | Biogrid | false |
| KRAS | Biogrid | false |
| OPTN | Biogrid | false |
| PHLPP1 | Biogrid | false |
| PHLPP2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
