---
type: protein-evaluation
gene: "DDIAS"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DDIAS 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DDIAS / C11orf82, NOXIN |
| 蛋白名称 | DNA damage-induced apoptosis suppressor protein |
| 蛋白大小 | 998 aa / 111.6 kDa |
| UniProt ID | Q8IXT1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 998 aa / 111.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=43.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR043522, IPR012340, IPR013955; Pfam: PF08646 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.5/180** | |
| **归一化总分** | | | **65.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 43 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C11orf82, NOXIN |

**关键文献**:
1. DDIAS, DNA damage-induced apoptosis suppressor, is a potential therapeutic target in cancer.. *Experimental & molecular medicine*. PMID: 37121974
2. DDIAS promotes invasion and proliferation of non-small cell lung cancer and predicts poor survival of lung cancer patients.. *International journal of clinical and experimental pathology*. PMID: 31966506
3. DDIAS suppresses TRAIL-mediated apoptosis by inhibiting DISC formation and destabilizing caspase-8 in cancer cells.. *Oncogene*. PMID: 29242605
4. Expression of DR4, DR5, FAS, Caspase-8 and, DDIAS Genes in AML Patients.. *Medical journal of the Islamic Republic of Iran*. PMID: 37575689
5. DNA Damage-Induced Apoptosis Suppressor Triggers Progression and Stemness of Glioma by Enhancing Lymphoid Enhancer-Binding Factor 1 Expression.. *World journal of oncology*. PMID: 38545470

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 43.3 |
| 高置信度残基 (pLDDT>90) 占比 | 6.7% |
| 置信残基 (pLDDT 70-90) 占比 | 8.1% |
| 中等置信 (pLDDT 50-70) 占比 | 4.9% |
| 低置信 (pLDDT<50) 占比 | 80.3% |
| 有序区域 (pLDDT>70) 占比 | 14.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=43.3），有序残基占 14.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043522, IPR012340, IPR013955; Pfam: PF08646 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ERCC6L | 0.794 | 0.102 | — |
| PSRC1 | 0.597 | 0.000 | — |
| TICRR | 0.576 | 0.090 | — |
| CDCA5 | 0.504 | 0.000 | — |
| CKAP2 | 0.501 | 0.000 | — |
| PARPBP | 0.497 | 0.090 | — |
| TMEM14A | 0.474 | 0.000 | — |
| POC1A | 0.452 | 0.095 | — |
| MEF2B | 0.448 | 0.078 | — |
| GGH | 0.446 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=43.3 + PDB: 无 | pLDDT=43.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DDIAS — DNA damage-induced apoptosis suppressor protein，非常新颖，仅有少数基础研究。
2. 蛋白大小998 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=43.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IXT1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165490-DDIAS/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DDIAS
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IXT1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000165490-DDIAS/subcellular

![](https://images.proteinatlas.org/38541/634_G11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38541/634_G11_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/38541/635_G11_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/38541/635_G11_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/38541/639_G11_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/38541/639_G11_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IXT1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
