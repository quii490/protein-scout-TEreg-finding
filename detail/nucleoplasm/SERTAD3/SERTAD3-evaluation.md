---
type: protein-evaluation
gene: "SERTAD3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SERTAD3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SERTAD3 / RBT1 |
| 蛋白名称 | SERTA domain-containing protein 3 |
| 蛋白大小 | 196 aa / 21.8 kDa |
| UniProt ID | Q9UJW9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoli; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 196 aa / 21.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009263, IPR039585; Pfam: PF06031 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.0/180** | |
| **归一化总分** | | | **75.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 16 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RBT1 |

**关键文献**:
1. SERTAD3 induces proteasomal degradation of ZIKV capsid protein and represents a therapeutic target.. *Journal of medical virology*. PMID: 36594413
2. SERTAD3 interacts with porcine reproductive and respiratory syndrome virus nonstructural protein 9 and inhibits virus replication.. *International journal of biological macromolecules*. PMID: 40187446
3. The MGF360-16R ORF of African Swine Fever Virus Strain Georgia Encodes for a Nonessential Gene That Interacts with Host Proteins SERTAD3 and SDCBP.. *Viruses*. PMID: 31947814
4. MicroRNA-92a Targets SERTAD3 and Regulates the Growth, Invasion, and Migration of Prostate Cancer Cells via the P53 Pathway.. *OncoTargets and therapy*. PMID: 32606766
5. Analysis of chromatin accessibility in peripheral blood mononuclear cells from patients with early-stage breast cancer.. *Frontiers in pharmacology*. PMID: 39376611

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.8 |
| 高置信度残基 (pLDDT>90) 占比 | 17.9% |
| 置信残基 (pLDDT 70-90) 占比 | 27.0% |
| 中等置信 (pLDDT 50-70) 占比 | 29.6% |
| 低置信 (pLDDT<50) 占比 | 25.5% |
| 有序区域 (pLDDT>70) 占比 | 44.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.8），有序残基占 44.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009263, IPR039585; Pfam: PF06031 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RPA2 | 0.868 | 0.292 | — |
| STN1 | 0.783 | 0.000 | — |
| SERTAD2 | 0.644 | 0.000 | — |
| SERTAD4 | 0.642 | 0.000 | — |
| UBL5 | 0.592 | 0.591 | — |
| SNRPB | 0.591 | 0.591 | — |
| TMEM50A | 0.580 | 0.000 | — |
| USHBP1 | 0.539 | 0.539 | — |
| CDCA4 | 0.511 | 0.000 | — |
| SERTAD1 | 0.508 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| USHBP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| A0A0J1HYA4 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Q81N50 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A0A0G2RM27 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| pdpD2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| tolC | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ypeB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| APOA1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15174051|imex:IM-19123 |
| IGHA1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15174051|imex:IM-19123 |
| ENSP00000375882.3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.8 + PDB: 无 | pLDDT=66.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SERTAD3 — SERTA domain-containing protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小196 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=66.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UJW9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167565-SERTAD3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SERTAD3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UJW9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000167565-SERTAD3/subcellular

![](https://images.proteinatlas.org/68262/1409_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/68262/1409_C2_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/68262/1412_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/68262/1412_C2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/68262/1471_G4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/68262/1471_G4_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UJW9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UJW9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 26..73; /note="SERTA"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00396" |
| InterPro | IPR009263;IPR039585; |
| Pfam | PF06031; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000167565-SERTAD3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| RPA2 | Intact, Biogrid | true |
| USHBP1 | Intact, Biogrid | true |
| BEX2 | Intact | false |
| BFSP2 | Intact | false |
| C1orf216 | Intact | false |
| CCNC | Intact | false |
| CENPP | Intact | false |
| CEP19 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
