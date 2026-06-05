---
type: protein-evaluation
gene: "TXNDC9"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TXNDC9 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TXNDC9 / APACD |
| 蛋白名称 | Thioredoxin domain-containing protein 9 |
| 蛋白大小 | 226 aa / 26.5 kDa |
| UniProt ID | O14530 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm; Nucleus; Cytoplasm, cytoskeleton, microtubule org |
| 蛋白大小 | 10/10 | ×1 | 10 | 226 aa / 26.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=84.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036249, IPR013766; Pfam: PF00085 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **135.5/180** | |
| **归一化总分** | | | **75.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Enhanced |
| UniProt | Cytoplasm; Nucleus; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Midbody | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- midbody (GO:0030496)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: APACD |

**关键文献**:
1. Thioredoxin domain-containing protein 9 protects cells against UV-B-provoked apoptosis via NF-κB/p65 activation in cutaneous squamous cell carcinoma.. *Oncology research*. PMID: 37303736
2. TXNDC9 promotes hepatocellular carcinoma progression by positive regulation of MYC-mediated transcriptional network.. *Cell death & disease*. PMID: 30382079
3. TXNDC9 regulates oxidative stress-induced androgen receptor signaling to promote prostate cancer progression.. *Oncogene*. PMID: 31477836
4. Txndc9 Is Required for Meiotic Maturation of Mouse Oocytes.. *BioMed research international*. PMID: 28626760
5. High level of TXNDC9 predicts poor prognosis and contributes to the NF-κB-regulated metastatic potential in gastric cancer.. *Neoplasma*. PMID: 34846159

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.3 |
| 高置信度残基 (pLDDT>90) 占比 | 62.8% |
| 置信残基 (pLDDT 70-90) 占比 | 21.7% |
| 中等置信 (pLDDT 50-70) 占比 | 4.9% |
| 低置信 (pLDDT<50) 占比 | 10.6% |
| 有序区域 (pLDDT>70) 占比 | 84.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=84.3，有序区 84.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036249, IPR013766; Pfam: PF00085 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| INSR | 0.956 | 0.108 | — |
| KRT17 | 0.898 | 0.050 | — |
| YWHAG | 0.874 | 0.061 | — |
| HTT | 0.864 | 0.045 | — |
| TUBAL3 | 0.858 | 0.846 | — |
| YWHAE | 0.852 | 0.061 | — |
| SFN | 0.851 | 0.061 | — |
| YWHAH | 0.841 | 0.061 | — |
| YWHAB | 0.829 | 0.061 | — |
| TUBA1B | 0.820 | 0.804 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CHD3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CEP126 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SETDB1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| FEZ1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ELP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| IMMT | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PTN | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GIT1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| TUBA1A | psi-mi:"MI:0096"(pull down) | pubmed:29568061|imex:IM-26301 |
| COX14 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.3 + PDB: 无 | pLDDT=84.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cytoplasm, cytoskeleton, micro / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TXNDC9 — Thioredoxin domain-containing protein 9，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小226 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O14530
- Protein Atlas: https://www.proteinatlas.org/ENSG00000115514-TXNDC9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TXNDC9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O14530
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (enhanced)。来源: https://www.proteinatlas.org/ENSG00000115514-TXNDC9/subcellular

![](https://images.proteinatlas.org/31846/542_F7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/31846/542_F7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/31846/544_F7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/31846/544_F7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/31846/571_F7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/31846/571_F7_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O14530-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
