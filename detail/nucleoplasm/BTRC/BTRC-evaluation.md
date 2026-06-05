---
type: protein-evaluation
gene: "BTRC"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BTRC — REJECTED (研究热度过高 (PubMed strict=112，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BTRC / BTRCP, FBW1A, FBXW1A |
| 蛋白名称 | F-box/WD repeat-containing protein 1A |
| 蛋白大小 | 605 aa / 68.9 kDa |
| UniProt ID | Q9Y297 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Plasma membrane, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 605 aa / 68.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=112 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=79.7; PDB: 1P22, 2P64, 6M90, 6M91, 6M92, 6M93, 6M94 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR021977, IPR036047, IPR001810, IPR050995, IPR015 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.5/180** | |
| **归一化总分** | | | **51.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane, Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- SCF ubiquitin ligase complex (GO:0019005)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 112 |
| PubMed broad count | 347 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BTRCP, FBW1A, FBXW1A |

**关键文献**:
1. MAPK1/3 kinase-dependent ULK1 degradation attenuates mitophagy and promotes breast cancer bone metastasis.. *Autophagy*. PMID: 33213267
2. miR-224 targets BTRC and promotes cell migration and invasion in colorectal cancer.. *3 Biotech*. PMID: 33117626
3. Macrophage Gsα promotes NLRP3 stability and its intervention attenuates abdominal aortic aneurysm in male mice.. *Nature communications*. PMID: 41927545
4. Exosomal GPT2 derived from triple-negative breast cancer cells promotes metastasis by activating BTRC.. *Thoracic cancer*. PMID: 37287397
5. Hsa_circ_0000479 promotes gastric cancer progression by inhibiting BTRC-mediated ubiquitination of G3BP1.. *Experimental cell research*. PMID: 40320200

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.7 |
| 高置信度残基 (pLDDT>90) 占比 | 62.3% |
| 置信残基 (pLDDT 70-90) 占比 | 11.1% |
| 中等置信 (pLDDT 50-70) 占比 | 5.5% |
| 低置信 (pLDDT<50) 占比 | 21.2% |
| 有序区域 (pLDDT>70) 占比 | 73.4% |
| 可用 PDB 条目 | 1P22, 2P64, 6M90, 6M91, 6M92, 6M93, 6M94, 6TTU |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1P22, 2P64, 6M90, 6M91, 6M92, 6M93, 6M94, 6TTU）+ AlphaFold极高置信度预测（pLDDT=79.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR021977, IPR036047, IPR001810, IPR050995, IPR015943; Pfam: PF12125, PF12937, PF00400 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKP1 | 0.999 | 0.999 | — |
| CTNNB1 | 0.999 | 0.999 | — |
| NFKBIA | 0.999 | 0.995 | — |
| RBX1 | 0.999 | 0.959 | — |
| CUL1 | 0.999 | 0.999 | — |
| AXIN1 | 0.999 | 0.843 | — |
| GSK3B | 0.999 | 0.971 | — |
| SKP2 | 0.998 | 0.292 | — |
| APC | 0.998 | 0.787 | — |
| FBXW11 | 0.993 | 0.841 | — |

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
| 三维结构 | AlphaFold pLDDT=79.7 + PDB: 1P22, 2P64, 6M90, 6M91, 6M92,  | pLDDT=79.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. BTRC — F-box/WD repeat-containing protein 1A，研究基础较多，新颖性有限。
2. 蛋白大小605 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 112 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 112 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y297
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166167-BTRC/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BTRC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y297
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000166167-BTRC/subcellular

![](https://images.proteinatlas.org/31156/330_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/31156/330_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/31156/331_G1_3_red_green.jpg)
![](https://images.proteinatlas.org/31156/331_G1_4_red_green.jpg)
![](https://images.proteinatlas.org/31156/333_G1_5_red_green.jpg)
![](https://images.proteinatlas.org/31156/333_G1_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y297-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
