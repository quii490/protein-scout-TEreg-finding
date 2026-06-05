---
type: protein-evaluation
gene: "LYST"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## LYST — REJECTED (研究热度过高 (PubMed strict=211，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LYST / CHS, CHS1 |
| 蛋白名称 | Lysosomal-trafficking regulator |
| 蛋白大小 | 3801 aa / 429.1 kDa |
| UniProt ID | Q99698 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Plasma membrane, Centriolar satellite; UniProt: Cytoplasm |
| 蛋白大小 | 0/10 | ×1 | 0 | 3801 aa / 429.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=211 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016024, IPR000409, IPR036372, IPR050865, IPR023 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **58.0/180** | |
| **归一化总分** | | | **32.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane, Centriolar satellite | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- microtubule cytoskeleton (GO:0015630)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 211 |
| PubMed broad count | 370 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CHS, CHS1 |

**关键文献**:
1. Chediak-Higashi syndrome.. *Current opinion in hematology*. PMID: 37254856
2. Chediak-Higashi syndrome.. *Current opinion in hematology*. PMID: 18043242
3. Frequency and spectrum of disease-causing variants in 1892 patients with suspected genetic HLH disorders.. *Blood advances*. PMID: 32542393
4. Chediak-Higashi Syndrome.. **. PMID: 29939658
5. Chedíak-Higashi Syndrome: Hair-to-toe spectrum.. *Seminars in pediatric neurology*. PMID: 39622608

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.0 |
| 高置信度残基 (pLDDT>90) 占比 | 16.8% |
| 置信残基 (pLDDT 70-90) 占比 | 33.2% |
| 中等置信 (pLDDT 50-70) 占比 | 13.3% |
| 低置信 (pLDDT<50) 占比 | 36.7% |
| 有序区域 (pLDDT>70) 占比 | 50.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=64.0），有序残基占 50.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016024, IPR000409, IPR036372, IPR050865, IPR023362; Pfam: PF02138, PF14844, PF00400 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VTA1 | 0.948 | 0.255 | — |
| UNC13D | 0.829 | 0.000 | — |
| STX11 | 0.817 | 0.000 | — |
| AP3B1 | 0.805 | 0.071 | — |
| STXBP2 | 0.792 | 0.000 | — |
| RAB27A | 0.787 | 0.000 | — |
| HPS5 | 0.754 | 0.000 | — |
| HPS3 | 0.742 | 0.000 | — |
| PIK3R4 | 0.718 | 0.000 | — |
| SH2D1A | 0.689 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| A0A0F7RA44 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| Vamp2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Ccdc9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Dync1li1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| TACC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Cep85l | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Tnpo1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| LLGL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| KIF1C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.0 + PDB: 无 | pLDDT=64.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm; 额外: Plasma membrane, Centriolar satel | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. LYST — Lysosomal-trafficking regulator，研究基础较多，新颖性有限。
2. 蛋白大小3801 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 211 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=64.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 211 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99698
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143669-LYST/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LYST
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99698
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000143669-LYST/subcellular

![](https://images.proteinatlas.org/53366/806_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/53366/806_C2_3_red_green.jpg)
![](https://images.proteinatlas.org/53366/810_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/53366/810_C2_2_red_green.jpg)
![](https://images.proteinatlas.org/53366/838_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/53366/838_B10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
