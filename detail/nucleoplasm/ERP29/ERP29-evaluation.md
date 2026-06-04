---
type: protein-evaluation
gene: "ERP29"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ERP29 — REJECTED (研究热度过高 (PubMed strict=167，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ERP29 / C12orf8, ERP28 |
| 蛋白名称 | Endoplasmic reticulum resident protein 29 |
| 蛋白大小 | 261 aa / 29.0 kDa |
| UniProt ID | P30040 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Microtubules; 额外: Nucleoplasm; UniProt: Endoplasmic reticulum lumen; Melanosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 261 aa / 29.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=167 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=83.3; PDB: 2QC7, 5V8Z, 5V90 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016855, IPR011679, IPR036356, IPR012883, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.0/180** | |
| **归一化总分** | | | **45.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Microtubules; 额外: Nucleoplasm | Uncertain |
| UniProt | Endoplasmic reticulum lumen; Melanosome | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell surface (GO:0009986)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum lumen (GO:0005788)
- melanosome (GO:0042470)
- membrane (GO:0016020)
- smooth endoplasmic reticulum (GO:0005790)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 167 |
| PubMed broad count | 193 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C12orf8, ERP28 |

**关键文献**:
1. Friend or foe: Endoplasmic reticulum protein 29 (ERp29) in epithelial cancer.. *FEBS open bio*. PMID: 25709888
2. Endoplasmic reticulum protein 29 (ERp29): An emerging role in cancer.. *The international journal of biochemistry & cell biology*. PMID: 20920593
3. Molecular Chaperone ERp29: A Potential Target for Cellular Protection in Retinal and Neurodegenerative Diseases.. *Advances in experimental medicine and biology*. PMID: 29721972
4. ERp29 Attenuates Nicotine-Induced Endoplasmic Reticulum Stress and Inhibits Choroidal Neovascularization.. *International journal of molecular sciences*. PMID: 37958506
5. The impact of ERP29 on the progression of pharyngeal squamous cell carcinoma.. *Scientific reports*. PMID: 39465248

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.3 |
| 高置信度残基 (pLDDT>90) 占比 | 56.3% |
| 置信残基 (pLDDT 70-90) 占比 | 28.0% |
| 中等置信 (pLDDT 50-70) 占比 | 1.5% |
| 低置信 (pLDDT<50) 占比 | 14.2% |
| 有序区域 (pLDDT>70) 占比 | 84.3% |
| 可用 PDB 条目 | 2QC7, 5V8Z, 5V90 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2QC7, 5V8Z, 5V90）+ AlphaFold高质量预测（pLDDT=83.3），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016855, IPR011679, IPR036356, IPR012883, IPR036249; Pfam: PF07749, PF07912 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ERO1A | 0.956 | 0.000 | — |
| ERO1B | 0.922 | 0.000 | — |
| HSP90B1 | 0.894 | 0.000 | — |
| CYP2S1 | 0.888 | 0.000 | — |
| CALR | 0.814 | 0.165 | — |
| HSPA5 | 0.783 | 0.259 | — |
| PDIA4 | 0.765 | 0.194 | — |
| CYP2F1 | 0.763 | 0.000 | — |
| HSPA4 | 0.750 | 0.052 | — |
| CANX | 0.744 | 0.190 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSRNOP00000001822.3 | psi-mi:"MI:0232"(transcriptional complementation a | pubmed:22665516|imex:IM-21436 |
| EBI-8762218 | psi-mi:"MI:0096"(pull down) | pubmed:22665516|imex:IM-21436 |
| Pik3cb | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| UBQLN4 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| IKBKE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218 |
| pip | psi-mi:"MI:0045"(experimental interaction detectio | pubmed:unassigned4 |
| KCNMA1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-15154|pubmed:22174833 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.3 + PDB: 2QC7, 5V8Z, 5V90 | pLDDT=83.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum lumen; Melanosome / Microtubules; 额外: Nucleoplasm | 一致 |
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
1. ERP29 — Endoplasmic reticulum resident protein 29，研究基础较多，新颖性有限。
2. 蛋白大小261 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 167 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 167 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P30040
- Protein Atlas: https://www.proteinatlas.org/ENSG00000089248-ERP29/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ERP29
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P30040
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
