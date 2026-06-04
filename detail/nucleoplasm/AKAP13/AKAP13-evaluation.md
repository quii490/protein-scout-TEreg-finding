---
type: protein-evaluation
gene: "AKAP13"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## AKAP13 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AKAP13 / BRX, HT31, LBC |
| 蛋白名称 | A-kinase anchor protein 13 |
| 蛋白大小 | 2813 aa / 307.6 kDa |
| UniProt ID | Q12802 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm, cytosol; Cytoplasm; Cytoplasm, cell cortex; Nucle |
| 蛋白大小 | 2/10 | ×1 | 2 | 2813 aa / 307.6 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=82 篇 (≤100→2) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=80.9; PDB: 2DRN, 2LG1, 4D0N, 4D0O, 6BCA |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR046349, IPR035899, IPR000219, IPR011993, IPR041 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **97.5/180** | |
| **归一化总分** | | | **54.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm, cytosol; Cytoplasm; Cytoplasm, cell cortex; Nucleus; Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell cortex (GO:0005938)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 82 |
| PubMed broad count | 155 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BRX, HT31, LBC |

**关键文献**:
1. Integrative causal inference illuminates gene-environment interactions linking endocrine disruptors to female infertility.. *Ecotoxicology and environmental safety*. PMID: 40663944
2. AKAP13 couples GPCR signaling to mTORC1 inhibition.. *PLoS genetics*. PMID: 34673774
3. AKAP13 Enhances CREB1 Activation by FSH in Granulosa Cells.. *Reproductive sciences (Thousand Oaks, Calif.)*. PMID: 36401072
4. InDel and CNV within the AKAP13 Gene Revealing Strong Associations with Growth Traits in Goat.. *Animals : an open access journal from MDPI*. PMID: 37685010
5. Protein Kinase A-induced tamoxifen resistance is mediated by anchoring protein AKAP13.. *BMC cancer*. PMID: 26272591

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.9 |
| 高置信度残基 (pLDDT>90) 占比 | 48.6% |
| 置信残基 (pLDDT 70-90) 占比 | 24.6% |
| 中等置信 (pLDDT 50-70) 占比 | 13.4% |
| 低置信 (pLDDT<50) 占比 | 13.4% |
| 有序区域 (pLDDT>70) 占比 | 73.2% |
| 可用 PDB 条目 | 2DRN, 2LG1, 4D0N, 4D0O, 6BCA |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2DRN, 2LG1, 4D0N, 4D0O, 6BCA）+ AlphaFold极高置信度预测（pLDDT=80.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR046349, IPR035899, IPR000219, IPR011993, IPR041020; Pfam: PF17838, PF00621, PF10522 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RHOA | 0.999 | 0.970 | — |
| GNA12 | 0.973 | 0.335 | — |
| GNA13 | 0.933 | 0.100 | — |
| ARHGEF1 | 0.926 | 0.074 | — |
| AKAP1 | 0.920 | 0.000 | — |
| ARHGEF11 | 0.920 | 0.074 | — |
| PRKACA | 0.908 | 0.596 | — |
| CTNNAL1 | 0.864 | 0.292 | — |
| PRKD1 | 0.858 | 0.292 | — |
| YWHAB | 0.796 | 0.592 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.9 + PDB: 2DRN, 2LG1, 4D0N, 4D0O, 6BCA | pLDDT=80.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Cytoplasm; Cytoplasm, cell cor / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. AKAP13 — A-kinase anchor protein 13，研究基础较多，新颖性有限。
2. 蛋白大小2813 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 82 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q12802
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170776-AKAP13/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AKAP13
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q12802
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
