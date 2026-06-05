---
type: protein-evaluation
gene: "EIF5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EIF5 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=173，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EIF5 |
| 蛋白名称 | Eukaryotic translation initiation factor 5 |
| 蛋白大小 | 431 aa / 49.2 kDa |
| UniProt ID | P55010 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; 额外: Plasma membrane, Primary cilium, Primary cilium; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 431 aa / 49.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=173 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=73.2; PDB: 2E9H, 2G2K, 2IU1, 8OZ0, 8PJ2, 8PJ3 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016024, IPR045196, IPR002735, IPR016189, IPR016 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **74.0/180** | |
| **归一化总分** | | | **41.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Plasma membrane, Primary cilium, Primary cilium tip | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- plasma membrane (GO:0005886)
- synapse (GO:0045202)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 173 |
| PubMed broad count | 255 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Disruption of adipocyte HIF-1α improves atherosclerosis through the inhibition of ceramide generation.. *Acta pharmaceutica Sinica. B*. PMID: 35847503
2. Oocyte-specific deletion of eukaryotic translation initiation factor 5 causes apoptosis of mouse oocytes within the early-growing follicles by mitochondrial fission defect-reactive oxygen species-DNA damage.. *Clinical and translational medicine*. PMID: 39113233
3. Translational Regulation in Hepatocellular Carcinogenesis.. *Drug design, development and therapy*. PMID: 34703211
4. Hepatitis C Virus Translation Regulation.. *International journal of molecular sciences*. PMID: 32230899
5. Overexpression of eIF5 or its protein mimic 5MP perturbs eIF2 function and induces ATF4 translation through delayed re-initiation.. *Nucleic acids research*. PMID: 27325740

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.2 |
| 高置信度残基 (pLDDT>90) 占比 | 30.2% |
| 置信残基 (pLDDT 70-90) 占比 | 35.5% |
| 中等置信 (pLDDT 50-70) 占比 | 12.3% |
| 低置信 (pLDDT<50) 占比 | 22.0% |
| 有序区域 (pLDDT>70) 占比 | 65.7% |
| 可用 PDB 条目 | 2E9H, 2G2K, 2IU1, 8OZ0, 8PJ2, 8PJ3 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2E9H, 2G2K, 2IU1, 8OZ0, 8PJ2, 8PJ3）+ AlphaFold极高置信度预测（pLDDT=73.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016024, IPR045196, IPR002735, IPR016189, IPR016190; Pfam: PF01873, PF02020 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EIF3I | 0.999 | 0.963 | — |
| EIF2S2 | 0.999 | 0.982 | — |
| EIF1 | 0.999 | 0.916 | — |
| EIF3G | 0.999 | 0.974 | — |
| EIF3B | 0.999 | 0.975 | — |
| EIF2S1 | 0.998 | 0.976 | — |
| EIF3C | 0.998 | 0.868 | — |
| EIF3J | 0.998 | 0.722 | — |
| EIF3A | 0.998 | 0.948 | — |
| EIF3D | 0.997 | 0.652 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Rap1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| Dmel\CG8539 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| IKBKE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PUM1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| NRGN | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| Not11 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| ptrB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| HSPB1 | psi-mi:"MI:0097"(reverse ras recruitment system) | imex:IM-20864|pubmed:25277244 |
| FN1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-14135|pubmed:19738201 |
| SLC30A4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.2 + PDB: 2E9H, 2G2K, 2IU1, 8OZ0, 8PJ2,  | pLDDT=73.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol; 额外: Plasma membrane, Primary cilium, Prim | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. EIF5 — Eukaryotic translation initiation factor 5，研究基础较多，新颖性有限。
2. 蛋白大小431 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 173 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P55010
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100664-EIF5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EIF5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P55010
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P55010-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
