---
type: protein-evaluation
gene: "C10orf71"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C10orf71 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C10orf71 / C10orf71 |
| 蛋白名称 | Cardiac-enriched FHL2-interacting protein |
| 蛋白大小 | 1435 aa / 156.5 kDa |
| UniProt ID | Q711Q0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Mitochondria; UniProt: Cytoplasm, myofibril, sarcomere, Z line |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 1435 aa / 156.5 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=41.8; PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052303, IPR027838; Pfam: PF15232 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 1 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.0/180** | |
| **归一化总分** | | | **62.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Mitochondria | Approved |
| UniProt | Cytoplasm, myofibril, sarcomere, Z line | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Z disc (GO:0030018)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C10orf71 |

**关键文献**:
1. Frameshift variants in C10orf71 cause dilated cardiomyopathy in human, mouse, and organoid models.. *The Journal of clinical investigation*. PMID: 38950288
2. Analysis of the lncRNA-Associated Competing Endogenous RNA (ceRNA) Network for Tendinopathy.. *Genetics research*. PMID: 35645614
3. Curcumin alleviates proliferation dysfunction in chicken granulosa cells under oxidative stress through AKT-Raf1-ERK1/2 signaling pathway.. *Poultry science*. PMID: 40544678
4. Discovery of novel heart rate-associated loci using the Exome Chip.. *Human molecular genetics*. PMID: 28379579
5. Morphometric analysis of nuclear shape irregularity as a novel predictor of programmed death-ligand 1 expression in lung squamous cell carcinoma.. *Virchows Archiv : an international journal of pathology*. PMID: 37171482

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 41.8 |
| 高置信度残基 (pLDDT>90) 占比 | 2.2% |
| 置信残基 (pLDDT 70-90) 占比 | 4.3% |
| 中等置信 (pLDDT 50-70) 占比 | 8.2% |
| 低置信 (pLDDT<50) 占比 | 85.3% |
| 有序区域 (pLDDT>70) 占比 | 6.5% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=41.8），有序残基占 6.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052303, IPR027838; Pfam: PF15232 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DYRK1A | 0.796 | 0.785 | — |
| DYRK1B | 0.771 | 0.759 | — |
| DCAF7 | 0.689 | 0.689 | — |
| CLPB | 0.680 | 0.402 | — |
| FNTB | 0.644 | 0.632 | — |
| FNTA | 0.631 | 0.628 | — |
| MYO18B | 0.614 | 0.091 | — |
| GRPEL2 | 0.588 | 0.306 | — |
| GRPEL1 | 0.588 | 0.306 | — |
| DNAJC10 | 0.566 | 0.305 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CEFIP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 1
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 1 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=41.8 + PDB: 无 | pLDDT=41.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, myofibril, sarcomere, Z line / Nucleoplasm; 额外: Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 1 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. C10orf71 — Cardiac-enriched FHL2-interacting protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1435 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=41.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q711Q0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177354-C10orf71/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C10orf71
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q711Q0
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 04:19:29

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000177354-C10orf71/subcellular

![](https://images.proteinatlas.org/57556/1377_E4_1_red_green.jpg)
![](https://images.proteinatlas.org/57556/1377_E4_2_red_green.jpg)
![](https://images.proteinatlas.org/57556/1413_E12_1_red_green.jpg)
![](https://images.proteinatlas.org/57556/1413_E12_3_red_green.jpg)
![](https://images.proteinatlas.org/57556/1854_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/57556/1854_A3_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
