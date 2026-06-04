---
type: protein-evaluation
gene: "ABI2"
date: 2026-05-28
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ABI2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | ABI2 / AblBP3, ArgBPIA, SSH3BP2, ABI-2, AIP-1, ArgBP1 |
| 蛋白大小 | 513 aa / 55663 Da |
| UniProt ID | Q9NYB9 |
| 评估日期 | 2026-05-28 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7 /10 | ×3 | 21 | Protein Atlas IF 显示主要定位于核质 (supported)；UniProt 列出细胞核；但蛋白主要功能为肌动蛋白调控，存在胞质信号 |
| 📏 蛋白大小 | 10 /10 | ×2 | 20 | 513 aa, 55.7 kDa, 处于 300-800 aa 理想区间 |
| 🆕 研究新颖性 | 5 /10 | ×3 | 15 | PubMed 227 篇 (1990 年起)；chromatin/epigenetics 仅 85 篇偏代谢/癌症方向，染色质调控方向几乎空白 |
| 🏗️ 三维结构 | 4 /10 | ×3 | 12 | pLDDT 平均 65.8，有序区仅 43.7%，46.8% 无序区域；PAE 均值 26.0 Å，高置信度区极少 (PAE<5 仅 5.5%)；有 5 个实验 PDB 结构覆盖折叠域 |
| 🧬 调控结构域 | 3 /10 | ×2 | 6 | SH3 结构域 + ABI homeo-domain homologous domain + SNARE coiled-coil；均为蛋白-蛋白互作域，无 DNA/染色质结合域；蛋白已被 200+ 文献研究，发现新型调控域可能性低 |
| 🔗 PPI ；0% 染色质/表观遗传调控 partner；与核定位推断相矛盾 |
| ➕ 互证加分 | — | max +3 | +1.5 | 定位 (IF+UniProt) +0.5；结构 (实验 PDB+AF) +0.5；结构域 (≥3 来源) +0.5；PPI 无双库可互证 |
| **原始总分** | | | **78.0 /158** |
| **归一化总分** | | | **49.4 /100** |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| Protein Atlas (IF) | **核质** (nucleoplasm, mainly) + 囊泡 (vesicles) + 胞质溶胶 (cytosol) | Supported |
| UniProt | 细胞质、细胞核、片状伪足、丝状伪足、细胞骨架、粘附连接 | ECO 证据 |
| GO (CC) | actin filament, filopodium tip, lamellipodium, SCAR complex, adherens junction | — |

![[Projects/TEreg-finding/protein-interested/detail/rejected/ABI2/IF_images/U2OS_1.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/ABI2/IF_images/PC3_1.jpg]]

**结论**: Protein Atlas IF 显示 ABI2 主要定位于核质 (nucleoplasm)，PC-3、SH-SY5Y、U2OS 三个细胞系均显示清晰核信号，附加胞质/囊泡信号。UniProt 亦列出细胞核定位。但蛋白已知功能为 WAVE 复合体组分参与肌动蛋白调控（胞质/细胞骨架功能），IF 显示的核定位可能是第二功能或定位富集。核定位得分 7，非淘汰。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/ABI2/IF_images/U2OS_2.jpg|U2OS_2]]

#### 3.2 蛋白大小评估
**评价**: 513 aa / 55.7 kDa，处于 300-800 aa 的理想区间，适合生化纯化、结构解析及功能实验，不存在技术性障碍。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 | 227 |
| 最早发表年份 | 1990 |
| Chromatin/epigenetics 相关 | 85 (38%) — 但多涉及癌症信号通路、细胞迁移等，非染色质调控本身 |

**主要研究方向**:
- 肌动蛋白细胞骨架调控 (WAVE 复合体/Arp2/3)
- 癌症侵袭与转移 (ABL 激酶信号)
- 神经元树突棘形态发生
- 细胞粘附连接组装

**评价**: 已有 227 篇文献，研究集中在肌动蛋白调控和癌症生物学。染色质/表观遗传方向几乎空白——尽管有 85 篇涉及 chromatin 关键词，但主要是癌症信号通路中的附属提及，非染色质调控本身的功能研究。这既是局限（核心功能不在此方向）也是潜在机会（若确有核功能则高度新颖）。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 65.8 |
| PDB 实验结构 | — |
| 有序区域 (pLDDT>70) 占比 | 43.7% (224/513 residues) |
| 高置信度 (pLDDT>90) | 39.2% (201 residues) |
| 低置信度/无序 (pLDDT<50) | 46.8% (240 residues) |
| 可用 PDB 实验结构 | 2ED0 (NMR), 3P8C (X-ray 2.29Å), 4N78 (X-ray 2.43Å), 7USC (EM 3Å), 7USD (EM 3Å) |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/ABI2/ABI2-PAE.png]]

**PAE 数值分析**:
- PAE 矩阵尺寸: 513 × 513
- PAE 总体均值: 26.0 Å（整体预测置信度低）
- PAE <5 Å 占比: 5.5%（极少高置信度区域）
- PAE <10 Å 占比: 8.7%
- N/C 半区间 PAE: 28.8 Å（域间关系不确定）
- 二级结构: α-helix ~15%、β-sheet ~10%、coil ~75%（估计值）

**评价**: 结构质量偏低。近半数残基 (46.8%) pLDDT <50，属无序区域。PAE 图整体噪声大，仅少量区域 (<10%) 有可靠的结构预测。值得注意的是，有 5 个实验 PDB 结构覆盖了折叠域（SH3 结构域等），说明折叠域本身结构确定，但大量长无序区 (IDR) 使整体结构质量下降。这种「折叠域+长无序区」的架构在信号支架蛋白中常见，但不利于基于结构的药物设计。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| InterPro | SH3 domain (IPR001452), ABI homeo-domain homologous domain (IPR012849), Target SNARE coiled-coil domain (IPR000727), SH3-like domain superfamily (IPR036028) |
| GeneCards | SH3 domain binding, proline-rich region binding, ubiquitin protein ligase binding |
| Pfam (via InterPro) | SH3_9 (Abl Interactor 2 SH3 domain), SH3_1 |

**染色质调控潜力分析**:
- **SH3 结构域**: 经典的蛋白-蛋白相互作用模块，识别富含脯氨酸的序列，与 DNA/染色质无直接关联。
- **ABI homeo-domain homologous domain (IPR012849)**: 值得注意的是，此结构域在三维结构上与 homeodomain 相似。Homeodomain 是 DNA 结合结构域，但 ABI 家族的 homeo-domain homologous domain 被特化为蛋白-蛋白互作域，目前无 DNA 结合实验证据。**若有核定位功能，该域的三维同源性提供了一定的 DNA/染色质结合潜力假说**，但属推测性。
- **SNARE coiled-coil domain**: 蛋白-蛋白互作，与膜融合相关。
- **结论**: 所有注释结构域均为蛋白-蛋白互作域，无 DNA/染色质结合的直接证据。考虑到 PubMed 已有 227 篇，发现全新 DNA 结合结构域的可能性低。得分 3。

#### 3.6 PPI :

Top 15 partners:

| Partner | Score | 功能类别 | 与调控相关？ |
|---|---|---|---|
| ABI1 | 0.996 | WAVE 复合体 | 否 |
| NCKAP1 | 0.999 | WAVE 复合体 | 否 |
| CYFIP1 | 0.999 | WAVE 复合体 | 否 |
| CYFIP2 | 0.999 | WAVE 复合体 | 否 |
| BRK1 | 0.999 | WAVE 复合体 | 否 |
| WASF1 | 0.999 | WAVE 复合体 | 否 |
| WASF2 | 0.999 | WAVE 复合体 | 否 |
| WASF3 | 0.995 | WAVE 复合体 | 否 |
| ABL1 | 0.981 | 酪氨酸激酶 | 否 |
| ABL2 | 0.770 | 酪氨酸激酶 | 否 |
| BAIAP2 | 0.970 | 肌动蛋白调控 | 否 |
| RAC1 | 0.966 | 小 GTPase | 否 |
| NCK1 | 0.818 | 衔接蛋白 | 否 |
| WAS | 0.873 | 肌动蛋白调控 | 否 |
| BCAR1 | 0.737 | 粘附/迁移 | 否 |

**humanPPI** (prodata.swmed.edu): 详见 STRING API 数据

**PPI 互证**:
- 两工具共同预测的调控相关 neighbor: N/A（humanPPI 数据缺失）
- STRING 调控相关比例: **0/30 (0%)**

**调控相关比例**: 0/30 (0%)

**评价**: PPI | 实验结构覆盖折叠域，AlphaFold 高置信度区域与实验结构吻合 | ✅ 一致 |

| 结构域 | UniProt / InterPro / Pfam / GeneCards | 均确认 SH3 + ABI-homeo 结构域，来源一致 | ✅ 一致 |
|---|---|---|---|
| PPI | STRING + humanPPI | humanPPI 数据缺失，仅 STRING 可用 | ⚠️ 无法互证 |
| 定位 | Protein Atlas IF + UniProt | 均确认核定位 | ✅ 一致 |
| 进化保守性 | UniProt | 小鼠直系同源物已知，功能保守 | ✅ |

**互证加分明细**:
- 定位互证：Protein Atlas IF (nucleoplasm) + UniProt (nucleus) → **+0.5**
- 三维结构互证：AlphaFold 折叠域 (pLDDT>90 区域) 有实验 PDB 结构 (2ED0, 3P8C 等) 验证 → **+0.5**
- 结构域互证：UniProt + InterPro + Pfam + GeneCards ≥3 来源检出 SH3/ABI 结构域 → **+0.5**
- PPI 互证：humanPPI 数据缺失，无法互证 → 0
- **总分**: **+1.5 / max +3**

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold + PDB | 见 3.4 节 | — |
| 结构域 | UniProt / InterPro / Pfam | 见 3.5 节 | — |
| PPI | STRING | 见 3.6 节 | — |
| 定位 | Protein Atlas IF / UniProt / GO | Nucleus | ✅ |

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**核心优势**:
1. Protein Atlas IF 显示清晰核定位 (nucleoplasm, supported)，且有 UniProt 佐证
2. 蛋白大小理想 (513 aa)，适合实验操作
3. 染色质调控方向几乎空白——若确存在核功能则高度新颖
4. ABI homeo-domain homologous domain 在三维结构上与 DNA 结合域同源，提供假说基础

**风险/不确定性**:
1. **核心功能为肌动蛋白细胞骨架调控**，PPI 在 Protein Atlas IF 中显示纯质膜定位，提示 ABI2 的核定位可能需要独立验证

**下一步建议**:
- [ ] 实验验证 ABI2 核定位（IF 重复 + 核质分离 Western blot）
- [ ] ChIP-seq / CUT&RUN 检测 ABI2 是否与染色质结合
- [ ] 核 interactome (BioID/APEX) 鉴定 ABI2 的核内互作伙伴
- [ ] 调查 ABI2 核定位的生物学条件（细胞周期依赖性？应激响应？）

### 5. 数据来源
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138443-ABI2/subcellular
- UniProt: https://www.uniprot.org/uniprotkb/Q9NYB9/
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22ABI2%22 (227 results)
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NYB9
- InterPro: https://www.ebi.ac.uk/interpro/protein/UniProt/Q9NYB9/
- STRING: https://string-db.org/network/9606.ENSP00000295851
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=ABI2
- PDB: 2ED0, 3P8C, 4N78, 7USC, 7USD

![[Projects/TEreg-finding/protein-interested/detail/rejected/ABI2/ABI2-PAE.png]]


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/ABI2/ABI2-PAE.png]]




