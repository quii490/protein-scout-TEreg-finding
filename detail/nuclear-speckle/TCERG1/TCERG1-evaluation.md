---
type: protein-evaluation
gene: "TCERG1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TCERG1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TCERG1 / CA150, TAF2S |
| 蛋白名称 | Transcription elongation regulator 1 |
| 蛋白大小 | 1098 aa / 123.9 kDa |
| UniProt ID | O14776 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 1098 aa / 123.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=34 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.8; PDB: 2DK7, 2DOD, 2DOE, 2DOF, 2E71, 2KIQ, 2KIS |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002713, IPR036517, IPR045148, IPR001202, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.5/180** | |
| **归一化总分** | | | **70.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 34 |
| PubMed broad count | 82 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CA150, TAF2S |

**关键文献**:
1. Huntingtin interactome reveals huntingtin role in regulation of double strand break DNA damage response (DSB/DDR), chromatin remodeling and RNA processing pathways.. *bioRxiv : the preprint server for biology*. PMID: 39763784
2. Huntingtin (HTT) interactome in regulation of DNA repair/remodeling and RNA processing pathways.. *Life science alliance*. PMID: 41850723
3. Epigenetic mechanisms governing cell type specific somatic expansion and toxicity in Huntington's disease.. *bioRxiv : the preprint server for biology*. PMID: 40501897
4. The in vivo dynamics of TCERG1, a factor that couples transcriptional elongation with splicing.. *RNA (New York, N.Y.)*. PMID: 26873599
5. Overexpression of TCERG1 as a prognostic marker in hepatocellular carcinoma: A TCGA data-based analysis.. *Frontiers in genetics*. PMID: 36299588

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.8 |
| 高置信度残基 (pLDDT>90) 占比 | 27.6% |
| 置信残基 (pLDDT 70-90) 占比 | 32.7% |
| 中等置信 (pLDDT 50-70) 占比 | 3.7% |
| 低置信 (pLDDT<50) 占比 | 36.0% |
| 有序区域 (pLDDT>70) 占比 | 60.3% |
| 可用 PDB 条目 | 2DK7, 2DOD, 2DOE, 2DOF, 2E71, 2KIQ, 2KIS, 2MW9, 2MWA, 2MWB |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.8），有序残基占 60.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002713, IPR036517, IPR045148, IPR001202, IPR036020; Pfam: PF01846, PF00397, PF23517 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PRPF38A | 0.995 | 0.966 | — |
| MFAP1 | 0.995 | 0.966 | — |
| SF3B4 | 0.995 | 0.979 | — |
| ZMAT2 | 0.993 | 0.966 | — |
| SF3A1 | 0.992 | 0.985 | — |
| SF3B1 | 0.991 | 0.981 | — |
| SNRPA1 | 0.989 | 0.984 | — |
| SF3A3 | 0.988 | 0.981 | — |
| SNW1 | 0.987 | 0.966 | — |
| CDC5L | 0.985 | 0.966 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BARD1 | psi-mi:"MI:0096"(pull down) | pubmed:15383276|mint:MINT-5217 |
| LUC7L | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| PIAS4 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| HTT | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| CHD3 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| SETDB1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| A0A0F7R8Z5 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| eprs1.S | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:20174651|imex:IM-17228 |
| eef1a1o.S | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:20174651|imex:IM-17228 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.8 + PDB: 2DK7, 2DOD, 2DOE, 2DOF, 2E71,  | pLDDT=67.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TCERG1 — Transcription elongation regulator 1，非常新颖，仅有少数基础研究。
2. 蛋白大小1098 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 34 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=67.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O14776
- Protein Atlas: https://www.proteinatlas.org/ENSG00000113649-TCERG1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TCERG1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O14776
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000113649-TCERG1/subcellular

![](https://images.proteinatlas.org/69752/1343_A8_2_red_green.jpg)
![](https://images.proteinatlas.org/69752/1343_A8_3_red_green.jpg)
![](https://images.proteinatlas.org/69752/1347_A8_2_red_green.jpg)
![](https://images.proteinatlas.org/69752/1347_A8_3_red_green.jpg)
![](https://images.proteinatlas.org/69808/1343_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/69808/1343_D9_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O14776-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
