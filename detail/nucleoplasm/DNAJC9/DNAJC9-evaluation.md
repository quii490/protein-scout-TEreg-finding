---
type: protein-evaluation
gene: "DNAJC9"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DNAJC9 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJC9 |
| 蛋白名称 | DnaJ homolog subfamily C member 9 |
| 蛋白大小 | 260 aa / 29.9 kDa |
| UniProt ID | Q8WXX5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Plasma membrane, Cytosol; UniProt: Nucleus; Cytoplasm; Cell membrane |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 260 aa / 29.9 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 🏗️ 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=85.4; PDB: 7CIZ, 7CJ0 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001623, IPR018253, IPR056453, IPR036869, IPR052 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **141.5/180** | |
| **归一化总分** | | | **78.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm; Cell membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular space (GO:0005615)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 26 |
| 别名(未计入scoring) |  |

**关键文献**:
1. DNAJC9 integrates heat shock molecular chaperones into the histone chaperone network.. *Molecular cell*. PMID: 33857403
2. DNAJC9 prevents CENP-A mislocalization and chromosomal instability by maintaining the fidelity of histone supply chains.. *The EMBO journal*. PMID: 38600242
3. DNAJC9 Binds to and Enhances the Transcription of Hepatitis B Virus cccDNA by Recruiting Histone H3.3.. *Journal of medical virology*. PMID: 40407066
4. DNAJC9 expression in basal-like and luminal A breast cancer subtypes predicts worse survival.. *Molecular biology reports*. PMID: 37422538
5. Unveiling the host arsenal: Interactome profiling of ALV-J p32 integrase reveals novel antiviral targets.. *International journal of biological macromolecules*. PMID: 41386616

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.4 |
| 高置信度残基 (pLDDT>90) 占比 | 50.4% |
| 置信残基 (pLDDT 70-90) 占比 | 38.5% |
| 中等置信 (pLDDT 50-70) 占比 | 5.0% |
| 低置信 (pLDDT<50) 占比 | 6.2% |
| 有序区域 (pLDDT>70) 占比 | 88.9% |
| 可用 PDB 条目 | 7CIZ, 7CJ0 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（7CIZ, 7CJ0）+ AlphaFold高质量预测（pLDDT=85.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001623, IPR018253, IPR056453, IPR036869, IPR052594; Pfam: PF00226, PF23302 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| H4C6 | 0.971 | 0.968 | — |
| FAM149B1 | 0.967 | 0.000 | — |
| CCT2 | 0.948 | 0.050 | — |
| CCT4 | 0.948 | 0.071 | — |
| CCT6A | 0.947 | 0.071 | — |
| CCT7 | 0.946 | 0.071 | — |
| MCM2 | 0.944 | 0.915 | — |
| TCP1 | 0.943 | 0.068 | — |
| CCT5 | 0.942 | 0.071 | — |
| CCT3 | 0.942 | 0.071 | — |

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
| 三维结构 | AlphaFold pLDDT=85.4 + PDB: 7CIZ, 7CJ0 | pLDDT=85.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cell membrane / Nucleoplasm; 额外: Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DNAJC9 — DnaJ homolog subfamily C member 9，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小260 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WXX5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000213551-DNAJC9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJC9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WXX5
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:18:02

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000213551-DNAJC9/subcellular

![](https://images.proteinatlas.org/35215/371_D1_3_red_green.jpg)
![](https://images.proteinatlas.org/35215/371_D1_4_red_green.jpg)
![](https://images.proteinatlas.org/35215/372_D1_1_red_green.jpg)
![](https://images.proteinatlas.org/35215/372_D1_2_red_green.jpg)
![](https://images.proteinatlas.org/35215/374_D1_1_red_green.jpg)
![](https://images.proteinatlas.org/35215/374_D1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
