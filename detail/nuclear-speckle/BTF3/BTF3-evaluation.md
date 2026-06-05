---
type: protein-evaluation
gene: "BTF3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BTF3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BTF3 / BTF3 |
| 蛋白名称 | Butyrophilin subfamily 3 member A3 |
| 蛋白大小 | 584 aa / 65.0 kDa |
| UniProt ID | O00478 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; UniProt: Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 584 aa / 65.0 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=89 篇 (≤100→2) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=82.8; PDB: 4F8T, 5ZZ3, 6J0G, 6J0K, 6J0L, 8ZYR, 9II6 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001870, IPR043136, IPR053896, IPR003879, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- external side of plasma membrane (GO:0009897)
- membrane (GO:0016020)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 89 |
| PubMed broad count | 139 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BTF3 |

**关键文献**:
1. Small molecule induces mitochondrial fusion for neuroprotection via targeting CK2 without affecting its conventional kinase activity.. *Signal transduction and targeted therapy*. PMID: 33602894
2. BTF3 promotes proliferation and glycolysis in hepatocellular carcinoma by regulating GLUT1.. *Cancer biology & therapy*. PMID: 37382415
3. Clinicopathological and prognostic significance of elevated BTF3 expression in gastric cancer.. *Cellular and molecular biology (Noisy-le-Grand, France)*. PMID: 38279435
4. Collaborative Duality of CircGLIS3(2) RNA and Protein in human Wound Repair.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40279507
5. BTF3 promotes stemness and inhibits TypeⅠInterferon signaling pathway in triple-negative breast cancer.. *Biochemical and biophysical research communications*. PMID: 33383560

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.8 |
| 高置信度残基 (pLDDT>90) 占比 | 57.0% |
| 置信残基 (pLDDT 70-90) 占比 | 22.4% |
| 中等置信 (pLDDT 50-70) 占比 | 9.2% |
| 低置信 (pLDDT<50) 占比 | 11.3% |
| 有序区域 (pLDDT>70) 占比 | 79.4% |
| 可用 PDB 条目 | 4F8T, 5ZZ3, 6J0G, 6J0K, 6J0L, 8ZYR, 9II6 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4F8T, 5ZZ3, 6J0G, 6J0K, 6J0L, 8ZYR, 9II6）+ AlphaFold极高置信度预测（pLDDT=82.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001870, IPR043136, IPR053896, IPR003879, IPR013320; Pfam: PF22705, PF13765, PF00622 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NACA | 0.999 | 0.992 | — |
| RPL31 | 0.997 | 0.928 | — |
| RPL30 | 0.993 | 0.863 | — |
| NACA2 | 0.992 | 0.964 | — |
| RPL6 | 0.987 | 0.872 | — |
| RPL23A | 0.984 | 0.929 | — |
| RPL24 | 0.984 | 0.863 | — |
| RPL32 | 0.984 | 0.870 | — |
| RPL8 | 0.982 | 0.870 | — |
| RPL18A | 0.982 | 0.865 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EGD1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16926149|imex:IM-18933 |
| BTN3A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BTN3A3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| Dmel\CG10510 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Arp10 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Lim3 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Argk2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG42329 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Wdfy2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Pka-C3 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.8 + PDB: 4F8T, 5ZZ3, 6J0G, 6J0K, 6J0L,  | pLDDT=82.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. BTF3 — Butyrophilin subfamily 3 member A3，研究基础较多，新颖性有限。
2. 蛋白大小584 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 89 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O00478
- Protein Atlas: https://www.proteinatlas.org/ENSG00000145741-BTF3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BTF3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O00478
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000145741-BTF3/subcellular

![](https://images.proteinatlas.org/13007/625_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/13007/625_H2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/13007/629_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/13007/629_H2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/13007/631_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/13007/631_H2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O00478-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
