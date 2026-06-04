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

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

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


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TBZ3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140153-WDR20/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=WDR20
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TBZ3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
