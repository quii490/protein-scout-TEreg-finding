---
type: protein-evaluation
gene: "NT5C3A"
date: 2026-06-02
tags: [protein-scout, critical-reopen, false-rejection-reevaluated, accepted-on-reeval]
status: reevaluated
reeval_result: ACCEPT
original_rejection: "核定位证据弱 (3/10) - 被误判为纯胞质蛋白"
---

## NT5C3A -- RE-EVALUATED: ACCEPT (原始总分 132.0/180, 归一化 73.3/100)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NT5C3A (NT5C3, P5N1, UMPH1) |
| 蛋白名称 | Cytosolic 5'-nucleotidase 3A |
| 蛋白大小 | 336 aa / 37.9 kDa |
| UniProt ID | Q9H0P0 |
| 核定位 (HPA IF) | 无 IF 数据 (page_found_no_if_image_detected) |
| 核定位 (GO-CC) | nucleoplasm (IDA:HPA), nuclear body (IDA:HPA) |
| 评估日期 | 2026-06-02 |
| 原始淘汰原因 | 核定位证据弱 (误判为纯胞质蛋白) |

### 2. False Rejection Recheck

**原始淘汰判定**: 核定位得分 3/10 (定位 Cytoplasm + Endoplasmic reticulum) -> 因名称含 "Cytosolic" 被误判

**Recheck 发现**:

1. **名称误导**: "Cytosolic 5'-nucleotidase 3A" 的名称暗示纯胞质定位, 但 GO-CC 数据揭示丰富的核相关定位: nucleoplasm (GO:0005654, IDA:HPA) 和 nuclear body (GO:0016604, IDA:HPA)。两个 GO 注释均为 IDA 级别 (inferred from direct assay), 来自 HPA 实验数据。该蛋白虽以胞质为主, 但确实存在于细胞核和核体中。

2. **功能与核过程的关联**: 关键文献 (Al-Haj & Khabar, 2018, *Science Signaling*, PMID: 29463777) 报道 NT5C3A 是 interferon 和 cytokine 信号传导的负性表观遗传因子。该功能天然需要核定位或核质穿梭。

3. **蛋白结构与数据质量优异**: AlphaFold pLDDT=91.8 (极高), 83.3% 残基 pLDDT>90, 同时有 3 个 PDB 实验结构 (2CN1, 2JGA, 2VKQ)。结构数据质量在本次评估的 8 个基因中名列前茅。

4. **研究新颖性极佳**: PubMed strict count = 16 篇 (<20), 在 8 个重评基因中最低。虽然研究较少, 但有关键研究指出其表观遗传调控功能。

**结论**: 原始评估因名称含 "Cytosolic" 而错误地将核定位得分定为 3/10。GO-CC 有 IDA 级别的 nucleoplasm 和 nuclear body 证据, 加上 2018 年 Science Signaling 论文明确指出其表观遗传调控功能, 核定位得分应上调为 5/10。配合研究新颖性 10/10 和结构数据 9/10, 总分达 132/180, 强烈建议 ACCEPT。

### 3. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 5/10 | x4 | 20 | GO: nucleoplasm (IDA:HPA), nuclear body (IDA:HPA); 名称含"Cytosolic"但GO实验证据指向核定位 |
| 蛋白大小 | 10/10 | x1 | 10 | 336 aa / 37.9 kDa (理想范围 200-800 aa) |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=16 篇 (≤20 -> 10/10) |
| 三维结构 | 9/10 | x3 | 27 | AlphaFold v6 pLDDT=91.8, pct>90=83.3%; PDB: 2CN1/2JGA/2VKQ (X-ray) |
| 调控结构域 | 5/10 | x2 | 10 | IPR036412 (HAD-like), IPR023214 (HAD superfamily), IPR006434; Pfam PF05822 |
| PPI 网络 | 4/10 | x3 | 12 | STRING: NT5C family (database-driven); IntAct 15 互作 (pull-down 为主) |
| 互证加分 | -- | max +3 | 3.0 | PDB+AF(双源高质量) + STRING+IntAct + 结构域+AF + PDB多条目 |
| **原始总分** | | | **132.0/180** | |
| **归一化总分** | | | **73.3/100** | |

### 4. 详细分析

#### 4.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 无 IF 数据 (page_found_no_if_image_detected) | N/A |
| UniProt subcellular | Cytoplasm (ECO:0000305), Endoplasmic reticulum | Swiss-Prot |
| GO Cellular Component | nucleoplasm (GO:0005654, IDA:HPA); nuclear body (GO:0016604, IDA:HPA); cytoplasm (GO:0005737, IDA:UniProtKB); cytosol (GO:0005829, IDA:HPA); endoplasmic reticulum (GO:0005783, IDA:HPA); mitochondrion (GO:0005739, HTP:FlyBase) | 多层次证据 |

**核定位证据分析**:
- HPA IF 图像不可用, 无法通过免疫荧光直接确认定位
- UniProt 亚细胞定位仅标注 Cytoplasm 和 Endoplasmic reticulum
- **关键**: GO-CC 中 nucleoplasm 和 nuclear body 的 evidence code 均为 IDA:HPA, 表示 HPA 实验数据库中确实有该蛋白存在于核内和核体的直接实验证据
- 蛋白名称含 "Cytosolic" 可能源于其生化活性 (催化胞质核苷酸) 而非专指定位排他性
- 文献 (PMID:29463777) 报道其作为 "negative epigenetic factor in interferon and cytokine signaling" -- 表观遗传调控功能天然涉及核内过程

**结论**: 核定位证据为混合型 (以胞质为主, 但 GO IDA 证据支持核内存在)。考虑其表观遗传调控功能, 核定位得分上调为 5/10。

#### 4.2 蛋白大小评估

| 参数 | 数值 |
|------|------|
| 氨基酸数 | 336 aa |
| 分子量 | 37.9 kDa |
| 理想范围 | 200-800 aa |

**评价**: 336 aa, 37.9 kDa, 处于理想实验范围的中间区。小到适合在大肠杆菌中高效表达, 大到结构域折叠完备。是实验友好的蛋白大小。

#### 4.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed symbol_only count | 18 |
| PubMed broad count | 38 |
| 别名(未计入scoring) | NT5C3, P5N1, UMPH1 |

**关键文献**:
1. Al-Haj L, Khabar KSA (2018). "The intracellular pyrimidine 5'-nucleotidase NT5C3A is a negative epigenetic factor in interferon and cytokine signaling." *Science Signaling*. PMID: 29463777
2. Yang S, Li A, Lv L et al. (2024). "Identification and Validation of Nicotinamide Metabolism-Related Gene Signatures as a Novel Prognostic Model for Hepatocellular Carcinoma." *OncoTargets and therapy*. PMID: 38827823
3. Wieske L, Michael MR, In 't Veld SGJG et al. (2024). "Proximity extension assay-based discovery of biomarkers for disease activity in chronic inflammatory demyelinating polyneuropathy." *Journal of neurology, neurosurgery, and psychiatry*. PMID: 37879899
4. Florentinus-Mefailoski A, Bowden P, Scheltens P et al. (2021). "The plasma peptides of Alzheimer's disease." *Clinical proteomics*. PMID: 34182925
5. Song Y, Huang F, Li X et al. (2022). "DIA-based quantitative proteomic analysis on the meat quality of porcine Longissimus thoracis et lumborum cooked by different procedures." *Food chemistry*. PMID: 34619635

**评价**: PubMed strict=16 篇, 研究极为新颖。最关键的论文 (Al-Haj & Khabar, 2018) 发表于 Science Signaling, 首次揭示其表观遗传调控功能, 开辟了新的研究方向。由于文献极少, 该蛋白存在巨大的未探索空间。在本次 8 个重评基因中研究新颖性得分最高 (10/10)。

#### 4.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.8 |
| 高置信度残基 (pLDDT>90) 占比 | 83.3% |
| 置信残基 (pLDDT 70-90) 占比 | 6.5% |
| 中等置信 (pLDDT 50-70) 占比 | 8.0% |
| 低置信 (pLDDT<50) 占比 | 2.1% |
| 有序区域 (pLDDT>70) 占比 | 89.8% |
| 可用 PDB 条目 | 2CN1 (X-ray 2.67A), 2JGA (X-ray 3.01A), 2VKQ (X-ray 2.50A), 均覆盖 64-336 残基 |

**评价**: AlphaFold 预测质量极高 (mean pLDDT=91.8), 83.3% 残基 >90 置信度。3 个 PDB 实验结构覆盖催化结构域 (64-336, >80% 全长), 分辨率 2.50-3.01A。结构数据质量在本次评估中处于第一梯队 (仅次于 NQO2)。

#### 4.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR036412 (HAD-like superfamily), IPR023214 (HAD superfamily), IPR006434 (5'-nucleotidase) |
| Pfam | PF05822 (5-nucleotidase, N-terminal) |

**染色质调控潜力分析**: NT5C3A 属于 HAD (haloacid dehalogenase) 超家族, 具有磷酸水解酶活性。虽然其结构域主要是催化性的 (5'-nucleotidase), 但 2018 年的 Science Signaling 论文揭示其作为表观遗传因子的非酶学功能, 提示该蛋白可能通过蛋白-蛋白互作或非催化机制调控基因表达。此功能尚未在结构域水平得到注释, 未来研究可探索其调控结构域。

#### 4.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NT5C | 0.995 | 0 | 5'-nucleotidase 家族 |
| NT5M | 0.976 | 0 | 5'-nucleotidase 线粒体 |
| NT5C2 | 0.961 | 0 | 5'-nucleotidase 家族 |
| NT5C1A | 0.957 | 0 | 5'-nucleotidase 家族 |
| DCK | 0.947 | 0 | 脱氧胞苷激酶 |
| CMPK2 | 0.939 | 0 | 胞苷酸激酶 |
| CDA | 0.933 | 0 | 胞苷脱氨酶 |
| ENPP3 | 0.933 | 0 | 核苷酸焦磷酸酶 |
| DCTD | 0.930 | 0 | 脱氧胞苷酸脱氨酶 |
| UMPS | 0.929 | 0 | UMP 合成酶 |

**实验验证互作** (IntAct, 精选):

| Partner | 方法 | PMID |
|---------|------|------|
| RAB11B | anti tag coimmunoprecipitation | 28514442 |
| ACAA2 | pull down | 30833792 |
| TUFM | pull down | 30833792 |
| SUCLG1 | pull down | 30833792 |
| ALDH18A1 | pull down | 30833792 |
| PCK2 | pull down | 30833792 |
| AARS2 | pull down | 30833792 |
| MTHFD1L | pull down | 30833792 |
| COQ8A | pull down | 30833792 |
| VANGL1 | two hybrid array | 21988832 |

**PPI 互证分析**:
- STRING 预测互作主要集中在核苷酸代谢相关酶 (多为 database-derived)
- IntAct 互作涉及多种代谢酶 (线粒体、氨基酸代谢), 以 pull-down 为主要方法
- 没有显著的转录调控或表观遗传相关互作伙伴
- STRING partners: 15, IntAct interactions: 15

**评价**: PPI 网络以代谢酶为主, 缺乏转录调控相关的互作伙伴。这与其已知的酶学功能一致, 但未反映最近发现的表观遗传调控功能。PPI 网络有限但数据充分。

#### 4.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.8 + PDB 3 entries | pLDDT=91.8, v6, 3 PDB (64-336) | 预测+实验 (高度一致) |
| 定位 | UniProt + GO-CC | Cytoplasm+ER / nucleoplasm+nuclear body+cytoplasm | 部分一致 (GO 揭示核定位, UniProt 未收录) |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证 (3 个实验结构 + 高质量预测, pLDDT=91.8): +1.0
- 多库定位一致: +0 (UniProt 未收录核定位, GO 有)
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 高质量预测一致性: +0.5
- PDB 多条目覆盖 (3 entries): +1.0
**总分**: +3.0 / max +3

### 5. 总体评价

**推荐等级**: ACCEPT (原始评估 REJECTED -> 重新评估 ACCEPT)

**核心优势**:
1. 研究新颖性极优: PubMed strict=16 篇, 在本次 8 个重评基因中最低, 探索空间巨大
2. 结构数据质量极高: AlphaFold pLDDT=91.8 + 3 个 PDB 实验结构
3. 功能方向独特: 2018 年 Science Signaling 揭示其作为 interferon/cytokine 信号传导的表观遗传负调控因子, 该方向几乎未被后续研究发掘
4. 蛋白大小理想 (336 aa, 37.9 kDa), 实验友好

**风险/不确定性**:
1. 核定位证据不是传统的 IF 图像确认, 而是依赖 GO-CC IDA 注释, 需要通过实验进一步验证
2. 表观遗传调控功能的分子机制完全不清楚 -- 是否是直接染色质结合? 是否通过蛋白互作间接调控?
3. PPI 网络以代谢酶为主, 缺乏转录调控相关互作伙伴
4. 文献数极少 (16 篇), 这既是优势也是风险 -- 功能研究基础薄弱

**False Rejection 定性**:
原始评估因蛋白名称含 "Cytosolic" 而机械地将核定位得分定为 3/10, 忽视了 GO-CC 中 IDA:HPA 级别的 nucleoplasm 和 nuclear body 证据, 以及 Science Signaling 论文报道的表观遗传调控功能。修正核定位得分后, 配合其卓越的研究新颖性 (10/10) 和结构数据 (9/10), 总分达到 132.0/180, 属于强 ACCEPT。

**下一步建议**:
- [ ] 通过 IF 实验确认 NT5C3A 的核定位 (使用特异性抗体)
- [ ] 基于 Al-Haj & Khabar (2018) 的表观遗传功能发现, 设计 ChIP-seq 或 Cut&Run 验证其染色质结合
- [ ] 利用 3 个现有 PDB 结构 + AlphaFold 高质量预测, 设计结构导向的功能突变体
- [ ] 探索 NT5C3A 非酶学功能的分子机制 (如是否作为 scaffolds 或 adaptor)

### 6. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H0P0
- Protein Atlas: https://www.proteinatlas.org/search/NT5C3A
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NT5C3A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H0P0
- STRING: https://string-db.org/network/9606.ENSP00000326212
- Data fetched live: 2026-06-02
